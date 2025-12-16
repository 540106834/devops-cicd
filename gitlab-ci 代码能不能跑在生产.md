这份 `.gitlab-ci.yml` 看起来简单，**实际发生的是一整段“一次性微型服务器的诞生与消失”**。
我按**时间轴**把它完整展开，你会看到每一步在 Runner 里发生了什么 🎬

---

# 一、Pipeline 被创建的那一刻

当你 `git push` 到分支时，GitLab 做了三件事：

1. 发现仓库根目录有 `.gitlab-ci.yml`
2. 解析 `stages` 和 job
3. 创建一个 pipeline，其中只有一个 stage：`test`

```yaml
stages:
  - test
```

👉 这一步还**没跑任何命令**，只是“排好日程”。

---

# 二、Runner 接手 Job（关键转折点）

GitLab 找到一个**可用 Runner**，然后告诉它：

> “来，有个叫 `flask-health-check` 的 job 归你了。”

---

## 1️⃣ 启动一个全新的运行环境

```yaml
image: python:3.11
```

如果你用的是 **Docker executor**，这一步意味着：

* Runner 执行：

  ```bash
  docker pull python:3.11
  ```
* 创建一个**全新的容器**
* 这个容器：

  * 干净
  * 没有你的代码
  * 没有依赖
  * 没有进程

👉 这是一次性沙盒 🧪

---

## 2️⃣ 拉取你的项目代码

在 `script` 执行前，GitLab 自动做：

```text
git clone https://gitlab.com/xxx/xxx.git
git checkout <当前 commit>
```

代码被放进容器内的一个工作目录，例如：

```text
/builds/your-group/your-project/
```

---

# 三、`script` 开始执行（逐行剖解）

现在，我们进入你真正关心的部分。

---

## ① 安装依赖

```bash
pip install --no-cache-dir -r requirements.txt
```

### 实际发生的事

* 使用容器内的 `python` 和 `pip`
* 从 PyPI 下载 Flask 等依赖
* 安装到 **当前容器的 Python 环境**

关键点：

* ❌ 不会影响宿主机
* ❌ 不会被下一个 job 复用
* ✅ 只存在于这个 job 生命周期内

---

## ② 后台启动 Flask

```bash
python app.py &
```

### 实际发生的事

* `python app.py` 启动 Flask
* `&` 把进程放到**后台**
* Flask 监听：

  ```text
  0.0.0.0:8000
  ```

此时容器内状态是：

* 一个 Flask 进程在跑
* Shell 没被阻塞
* Job 继续往下执行

⚠️ 如果不加 `&`：

* Job 会卡在这里
* 后面的命令永远不执行

---

## ③ 等服务启动

```bash
sleep 3
```

### 实际发生的事

* Shell 暂停 3 秒
* 给 Flask 预留启动时间

这是一个**最朴素但不优雅的等待机制** 😅

如果 Flask 启动慢：

* 3 秒不够
* 健康检查会失败

---

## ④ 健康检查（判生死）

```bash
curl http://127.0.0.1:8000/health
```

### 实际发生的事

* 在**同一个容器**里
* 用 `curl` 请求 Flask
* 命中 `@app.route("/health")`
* Flask 返回：

  ```json
  {"status": "ok"}
  ```

### 成功 or 失败的判定

* HTTP 200 → 命令成功 → job 继续
* 连接失败 / 非 2xx → `curl` 返回非 0 → job 失败 ❌

👉 GitLab 用 **Shell 返回码** 判断 CI 成败

---

# 四、Job 结束时发生的事（很多人忽略）

当 `script` 全部执行完：

1. Flask 后台进程被**强制终止**
2. Docker 容器被**删除**
3. 所有依赖、日志、进程全部消失

```text
容器 = 用完即焚
```

---

# 五、这一段 CI 在“验证”什么

它验证的不是“代码能不能跑在生产”，而是：

* Flask 能正常启动
* 依赖没问题
* `/health` 路由可访问
* 基本运行逻辑没炸

👉 这是一个 **最小存活测试（Smoke Test）**

---

# 六、这份 CI 的隐含前提（重要）

你的 `app.py` 必须：

```python
app.run(host="0.0.0.0", port=8000)
```

否则：

* Flask 只监听 `127.0.0.1`
* curl 永远连不上
* CI 永远红

---

# 七、可以优化的地方（进阶）

### 1️⃣ 用循环代替 `sleep`

```bash
for i in {1..10}; do
  curl -f http://127.0.0.1:8000/health && break
  sleep 1
done
```

---

### 2️⃣ 用 `curl -f` 明确失败

```bash
curl -f http://127.0.0.1:8000/health
```

---

### 3️⃣ 用 `pytest` 替代 curl（更标准）

```python
def test_health():
    assert requests.get("http://127.0.0.1:8000/health").status_code == 200
```

---

# 八、一句话总结

> **这不是“跑 Flask”，
> 而是在 CI 的一次性容器里，
> 临时孵化一个服务，
> 看它能不能活着回应世界。**

如果你愿意，下一步我可以帮你把这段 CI：

* 改造成 **Docker 镜像级测试**
* 或升级成 **并行 test + build 的标准流水线**

你想走哪一步？
