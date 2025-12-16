好，我们**不跳步、不抽象、不假设你“已经会了”**。
这一次是**从 0 到 1 的完整实走**，像带你从仓库门口一路走到镜像进仓库 📦➡️🐳
你只需要顺着走。

---

# GitLab CI 构建

## 从 0 开始完整走一遍（真·流水）

---

## 第 0 步：你现在“手里有什么”

我们假设你现在只有三样东西：

1️⃣ 一台能装 Docker 的机器（本地 / 云主机 都行）
2️⃣ 一个 GitLab 账号
3️⃣ 一个最简单的 Python Web 项目

如果你跟我一样，我们就开始。

---

## 第 1 步：准备代码（最小可跑项目）

### 1️⃣ 新建项目目录

```bash
mkdir gitlab-ci-demo
cd gitlab-ci-demo
```

---

### 2️⃣ 写一个最简单的 Python Web

`app.py`

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello GitLab CI 👋"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
```

---

### 3️⃣ requirements.txt

```text
flask
```

---

## 第 2 步：写 Dockerfile（构建目标）

这是 **CI 要帮你做的事情本体**。

`Dockerfile`

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY app.py .

EXPOSE 8000
CMD ["python", "app.py"]
```

你现在已经明确了：

> **CI 的目标 = 执行 docker build，得到镜像**

---

## 第 3 步：在 GitLab 创建项目

1️⃣ 打开 GitLab
2️⃣ New Project
3️⃣ Create blank project
4️⃣ 项目名：`gitlab-ci-demo`

---

### 本地初始化 Git

```bash
git init
git remote add origin https://gitlab.com/你的用户名/gitlab-ci-demo.git
```

---

### 提交代码

```bash
git add .
git commit -m "init project"
git push -u origin master
```

到这里：

✅ Git 仓库有代码
❌ 还 **没有 CI**

---

## 第 4 步：写 `.gitlab-ci.yml`（最核心）

这是**整个 CI 的灵魂文件**。

### 1️⃣ 新建文件

`.gitlab-ci.yml`

```yaml
stages:
  - build

build_image:
  stage: build
  image: docker:25
  services:
    - docker:25-dind
  script:
    - docker build -t myapp:1.0 .
```

---

### 2️⃣ 再次提交

```bash
git add .gitlab-ci.yml
git commit -m "add gitlab ci"
git push
```

---

## 第 5 步：这一次 push 发生了什么（重点）

你敲下 `git push` 的瞬间：

```text
你的电脑
  ↓
GitLab 仓库
  ↓
GitLab 发现 .gitlab-ci.yml
  ↓
创建 Pipeline
  ↓
寻找 Runner
```

⚠️ **如果没有 Runner，这一步会卡住**

---

## 第 6 步：安装 GitLab Runner（关键节点）

CI 跑不跑，**全靠 Runner**。

---

### 1️⃣ 在一台机器上装 Runner

（Linux 示例）

```bash
curl -L https://gitlab-runner-downloads.s3.amazonaws.com/latest/binaries/gitlab-runner-linux-amd64 \
  -o /usr/local/bin/gitlab-runner

chmod +x /usr/local/bin/gitlab-runner
```

---

### 2️⃣ 注册 Runner

```bash
gitlab-runner register
```

你会依次看到：

```
GitLab URL:
→ https://gitlab.com/

Registration token:
→ 项目 Settings → CI/CD → Runners

Executor:
→ docker

Docker image:
→ docker:25
```

这一步本质是：

> **把这台机器，卖给 GitLab 当劳动力**

---

## 第 7 步：CI 真正开始跑了

Runner 注册完成后：

1️⃣ GitLab 把 job 发给 Runner
2️⃣ Runner 拉起一个容器（docker:25）
3️⃣ 同时启动 docker:dind
4️⃣ 在容器里执行：

```bash
docker build -t myapp:1.0 .
```

你在 GitLab 页面会看到：

* Pipeline：Running → Passed
* Job 日志一行一行滚动

这是 CI 的“心跳声”。

---

## 第 8 步：把镜像推到仓库（完整 CI）

现在升级一步。

### 修改 `.gitlab-ci.yml`

```yaml
stages:
  - build

variables:
  IMAGE_NAME: $CI_REGISTRY_IMAGE
  IMAGE_TAG: $CI_COMMIT_SHORT_SHA

build:
  stage: build
  image: docker:25
  services:
    - docker:25-dind
  script:
    - docker login -u $CI_REGISTRY_USER -p $CI_REGISTRY_PASSWORD $CI_REGISTRY
    - docker build -t $IMAGE_NAME:$IMAGE_TAG .
    - docker push $IMAGE_NAME:$IMAGE_TAG
```

---

### 再 push 一次

```bash
git add .gitlab-ci.yml
git commit -m "push image"
git push
```

---

## 第 9 步：现在这条流水线已经是“工业级”

完整链路变成：

```text
git push
 ↓
GitLab Pipeline
 ↓
Runner 拉 job
 ↓
docker build
 ↓
docker push
 ↓
镜像进入仓库
```

这已经是：

* 标准 CI
* 企业级容器构建
* K8s / CD 的上游

---

## 第 10 步：你现在真正理解了什么

如果你现在回头看：

* `.gitlab-ci.yml` 是**命令剧本**
* Runner 是**执行者**
* image / services 决定**运行环境**
* script 就是**你平时手敲的命令**

你已经不是“用 CI”，而是：

> **知道 CI 为什么能跑、跑在哪里、失败卡在哪一层**

---

## 下一步，我可以继续带你走哪一段

你已经站在分水岭了，我给你三条“继续实走”的路：

1️⃣ **Runner 内部原理（拉 job 到底是怎么拉的）**
2️⃣ **CI 构建但不用 dind 的安全方案**
3️⃣ **在这条 CI 后面接 K8s CD（镜像 → Pod）**

你点哪条，我继续带你往前走 🚦
