这是 GitLab CI/CD 里**最核心、也最容易被误解**的一块。
我们把它讲成一条**“调度系统与工人”的真实通信链路**，你看完就不会再把职责搞混了 🔗

---
| 事情                  | 谁做     |
| ------------------- | ------ |
| 检测 `.gitlab-ci.yml` | GitLab |
| 解析 YAML / rules     | GitLab |
| 决定跑哪些 job           | GitLab |
| 拉代码                 | Runner |
| 执行 script           | Runner |
| 上传结果                | Runner |


# 一、一句话总览（先给全景）

> **GitLab Server 负责“想什么、派什么活”**
> **Runner 负责“怎么干、在哪干”**

两者之间只有一个关系：

> **Runner 主动来要活，Server 决定给不给**

没有反向连接，没有 Server 主动推任务。

---

# 二、核心交互模型（非常重要）

## 🧠 模型关键词：**Pull-based（拉取式）**

```
Runner  ──“我空闲了，有活吗？”──▶  GitLab Server
Runner  ◀──“有，这个 job 你来跑”──  GitLab Server
```

这点决定了整个安全与架构设计。

---

# 三、完整时间线（真实发生顺序）

我们从你 `git push` 开始，一步一步走。

---

## ① Developer → GitLab Server

```bash
git push origin main
```

GitLab Server 做的事：

1. 接收 push
2. 查找 `.gitlab-ci.yml`
3. 解析 YAML
4. 生成 pipeline
5. 拆成多个 job
6. 放入 job 队列（pending）

👉 **此时还没有 Runner 参与**

---

## ② Runner 定期向 Server 轮询（心跳 + 要活）

Runner 本身是一个**常驻进程**，在后台循环做一件事：

```text
“我在线，有没有 job 给我？”
```

技术上是：

* Runner → GitLab Server
* 通过 HTTPS API
* 携带：

  * runner token
  * runner tags
  * runner executor 类型

---

## ③ GitLab Server 决策是否派活

Server 会检查：

* Runner token 是否有效
* Runner 是否 enabled
* tag 是否匹配
* job 是否允许该 Runner 执行

如果不匹配：

```text
“你不合适，下一个”
```

如果匹配：

👉 **分配 job**

---

## ④ Server → Runner：下发 Job 描述

GitLab Server 返回给 Runner 的是：

* job id
* stage
* script
* image
* variables
* artifacts 规则
* cache 规则

⚠️ 注意关键点：

> **不是 `.gitlab-ci.yml` 原文**
> **而是已经解析、裁剪、决策后的 job 配置**

---

## ⑤ Runner 开始执行 Job

Runner 接到 job 后：

1. 准备执行环境

   * shell / docker / k8s executor
2. 拉取项目代码

   ```bash
   git clone
   git checkout <commit>
   ```
3. 执行 `script`
4. 收集日志
5. 上传 artifacts（如果有）

---

## ⑥ Runner → Server：持续回传状态

在 job 执行过程中：

* Runner 不断回传：

  * running
  * log output
  * success / failed

GitLab Server 负责：

* 在 UI 实时展示日志
* 记录 job 状态
* 决定 pipeline 走向

---

## ⑦ Job 完成，Runner 释放资源

* 容器销毁 / Pod 删除
* Runner 重新回到：

```text
“我空闲了，有活吗？”
```

循环继续 ♻️

---

# 四、通信为什么设计成“Runner 拉”

这是一个**安全与可扩展性设计**。

### 1️⃣ 安全原因

* Runner 可以在内网
* 不需要 GitLab Server 主动访问内网
* 防火墙只需放行 Runner → Server

### 2️⃣ 扩展原因

* 你可以随时增加 Runner
* 不需要改 GitLab Server 配置
* Runner 即插即用

---

# 五、Runner 永远“不知道”的事情

Runner **不知道也不关心**：

* 默认分支是啥
* rules 为什么生效
* 哪些 job 被跳过
* `.gitlab-ci.yml` 写了什么结构

它只知道：

> “我被安排干这个 job”

---

# 六、用一句话把职责钉死

| 模块               | 角色        |
| ---------------- | --------- |
| GitLab Server    | 调度中心 / 大脑 |
| `.gitlab-ci.yml` | 调度规则      |
| Runner           | 执行器 / 工人  |
| Executor         | 工人用的工具    |

---

# 七、一个非常形象的比喻（但不失真）

> **GitLab Server 是空管塔台**
> **Runner 是飞机**
>
> 塔台不去找飞机，
> 飞机起飞前会不断问：
> “我能起飞吗？跑哪条航线？”

---

# 八、常见误解澄清（快速）

* ❌ Runner 监听仓库变化
  ✅ Runner 只监听 Server

* ❌ Runner 解析 `.gitlab-ci.yml`
  ✅ 解析权在 Server

* ❌ Runner 主动拉 pipeline
  ✅ Runner 只拉 job

---

## 一句话收尾

> **GitLab CI 的本质不是“自动执行”，
> 而是一个中心化调度 + 去中心化执行的系统。**

如果你愿意，下一步我可以继续深入一层：

* 🔐 Runner token 的权限模型
* 🏷️ tag 是怎么参与调度决策的
* ☸️ Kubernetes Runner 的内部交互

你想继续哪一块？
