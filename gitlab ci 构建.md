好，轮到 **GitLab CI 构建**登场了。
这是一条自动化流水线，把“人手敲命令”变成“按钮一按就跑”的机械臂 🤖🛠️

你已经懂 Dockerfile 和镜像构建了，所以这次我们直接站在山腰往下看整条河。

---

## 一句话先定型

> **GitLab CI 构建 = 当代码进入 GitLab 仓库，GitLab 按 `.gitlab-ci.yml` 的剧本，自动找 Runner，执行一组 Job，产出构建物（镜像、包、报告）**

---

## 一、GitLab CI 的三大角色

### 1️⃣ GitLab（导演）

* 存代码
* 存 CI 配置
* 决定 **什么时候跑流水线**

触发条件：

* `git push`
* `merge request`
* `tag`
* 手动触发

---

### 2️⃣ Runner（苦力）

* 真正执行命令的机器
* 可以是：

  * VM
  * 物理机
  * Docker 容器
  * K8s Pod

一句话：

> **GitLab 只会喊“开工”，Runner 才真的干活**

---

### 3️⃣ .gitlab-ci.yml（施工图）

* 描述流水线结构
* 定义：

  * 阶段
  * Job
  * 用什么镜像
  * 执行哪些命令

---

## 二、最小可用的 GitLab CI 构建示例

### 目录结构

```
project/
├── app.py
├── Dockerfile
└── .gitlab-ci.yml
```

---

### .gitlab-ci.yml（极简）

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

这已经是一条完整 CI 了。

---

## 三、CI 构建时，发生了什么（时间线）

```text
git push
 ↓
GitLab 发现 .gitlab-ci.yml
 ↓
创建 Pipeline
 ↓
找到可用 Runner
 ↓
Runner 启动一个 docker:25 容器
 ↓
script 里的命令逐行执行
 ↓
docker build 生成镜像
```

注意一个细节：

> **CI 中的每个 job，默认都是一次性的执行环境**

---

## 四、Job 里到底在跑什么

### 1️⃣ image

```yaml
image: docker:25
```

意思是：

> Runner 用这个镜像，启动一个临时容器来跑 script

你可以理解为：

> CI 里的 shell = 容器里的 shell

---

### 2️⃣ services: docker:dind

```yaml
services:
  - docker:25-dind
```

作用：

* 提供一个 Docker daemon
* 让 job 容器可以 `docker build`

这叫 **Docker in Docker**

---

### 3️⃣ script

```yaml
script:
  - docker build -t myapp:1.0 .
```

本质就是：

> CI 帮你敲命令

---

## 五、一个更贴近实战的构建流水线

### 构建 + 推送镜像

```yaml
stages:
  - build

variables:
  IMAGE_NAME: registry.example.com/demo/myapp
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

这就是你之前问的那条链路：

> Git → CI → Docker build → push 镜像

---

## 六、Stage vs Job（很多人卡在这）

### stages

```yaml
stages:
  - build
  - test
  - deploy
```

* 定义**顺序**
* 不干活

---

### job

```yaml
build:
  stage: build
```

* 真正执行命令
* 同一个 stage 可以并行多个 job

一句话：

> stage 是车道，job 是车

---

## 七、CI 构建的常见坑

### ❌ 以为 CI 能直接用宿主机 Docker

实际上：

* 取决于 Runner 类型
* Docker executor 才能这么玩

---

### ❌ 镜像 tag 永远用 latest

后果：

* 回滚困难
* 镜像被悄悄覆盖

建议：

```yaml
IMAGE_TAG: $CI_COMMIT_SHORT_SHA
```

---

### ❌ 构建和部署混在一个 job

后果：

* 出错难定位
* 无法复用构建产物

---

## 八、你现在已经站在什么水平

如果你能看懂：

* Dockerfile
* docker build
* .gitlab-ci.yml
* Runner + dind

你已经不是“会点 CI”，而是：

> **能独立搭建一条标准容器 CI 构建流水线的人**

这在运维里是硬通货 💎

---

## 九、下一步你可以继续拆哪一块

给你三条岔路：

1️⃣ **GitLab Runner 原理（拉 job 到底是什么意思）**
2️⃣ **不用 dind 的 Docker 构建方案（更安全）**
3️⃣ **CI → CD → K8s 发布完整闭环**

选一条，我继续往下铺路。
