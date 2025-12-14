好，这里给你一份 **从零搭建 GitLab CI 环境的完整实操指南**。思路像搭舞台，GitLab 是导演，Runner 是演员，CI 脚本是剧本，Docker 是道具间 🎭。一步步来，不迷路。

------

## 一、CI 环境的基本构成

要让 GitLab 能跑 CI，需要 **三样东西同时就位**：

1. **GitLab CE**
   提供仓库、Pipeline、UI
2. **GitLab Runner**
   真正执行 CI Job 的执行器
3. **Executor（Docker）**
   Job 运行的沙盒环境

你现在的架构是 **同机 Docker 部署**，这是最常见、最稳妥的入门方案。

------

## 二、确认 GitLab 已就绪

### 1️⃣ 能访问 GitLab

浏览器访问：

```
http://<宿主机IP>/
```

确认你能：

- 登录（root）
- 创建项目
- push 代码

------

## 三、安装并注册 GitLab Runner

### 1️⃣ Runner 容器是否在运行

```bash
docker ps | grep gitlab-runner
```

有输出说明 Runner 已启动。

------

### 2️⃣ 获取 Runner 注册 Token

进入 GitLab：

```
项目 → Settings → CI/CD → Runners → Registration token
```

复制这个 token。

------

### 3️⃣ 注册 Runner

```bash
docker exec -it gitlab-runner gitlab-runner register
```

填写示例：

```
GitLab URL: http://gitlab/
Registration token: xxxxxx
Description: docker-runner
Tags: docker,ci
Executor: docker
Default Docker image: alpine:3.19
```

注册完成后，会生成：

```
./runner/config/config.toml
```

这一步就是 CI 的“通行证签发”。

------

### 4️⃣ 验证 Runner 状态

在 GitLab 页面：

```
项目 → Settings → CI/CD → Runners
```

你应该能看到：

✅ Runner 状态：**Active**

------

## 四、CI 的“引擎房”配置（Runner）

### Runner 核心配置在这里：

```bash
./runner/config/config.toml
```

关键内容示例：

```toml
concurrent = 1

[[runners]]
  name = "docker-runner"
  url = "http://gitlab/"
  token = "xxxxx"
  executor = "docker"

  [runners.docker]
    image = "alpine:3.19"
    privileged = true
    volumes = ["/cache", "/var/run/docker.sock:/var/run/docker.sock"]
```

### 关键解释

| 项目        | 含义                      |
| ----------- | ------------------------- |
| executor    | 使用 docker 方式跑 CI     |
| docker.sock | 允许 CI 构建镜像          |
| privileged  | Docker-in-Docker 场景必需 |
| concurrent  | 控制并发，防止机器被榨干  |

------

## 五、写第一个 `.gitlab-ci.yml`

这是 CI 的灵魂文件，**必须放在仓库根目录**。

### 最小可运行示例

```yaml
stages:
  - test

hello-ci:
  stage: test
  tags:
    - docker
  script:
    - echo "Hello GitLab CI"
    - uname -a
```

提交并 push：

```bash
git add .gitlab-ci.yml
git commit -m "add ci"
git push
```

------

## 六、Pipeline 启动的瞬间

推送后，GitLab 会自动发生这件事：

1. GitLab 解析 `.gitlab-ci.yml`
2. 创建 Pipeline
3. 根据 tags 找 Runner
4. Runner 拉起 Docker 容器
5. 执行 `script`

你可以在这里看结果：

```
CI/CD → Pipelines → Jobs
```

看到绿色 ✅，说明 CI 环境跑通了。

------

## 七、使用本地 Docker 镜像跑 CI（常见进阶）

### 1️⃣ 本地先构建镜像

```bash
docker build -t my-ci-image:latest .
```

### 2️⃣ 在 CI 中使用

```yaml
image: my-ci-image:latest

stages:
  - build

build-job:
  stage: build
  tags:
    - docker
  script:
    - echo "use local image"
```

只要 Runner 挂载了：

```
/var/run/docker.sock
```

就能直接用本地镜像，不走外网。

------

## 八、常见问题速查表

### ❌ Pipeline 一直 Pending

- Runner 没注册
- tags 不匹配
- Runner 被设为 paused

### ❌ Job 拉不到镜像

- 镜像不存在
- Runner 没权限访问 Docker

### ❌ CI 中无法 docker build

- 没挂 docker.sock
- privileged=false

------

## 九、推荐的 CI 成熟形态

当你玩熟了，可以进阶为：

- 多 Runner（构建 / 测试分离）
- 私有 Harbor / GitLab Registry
- 缓存加速（cache / artifacts）
- 自动发布到 K8s

------

## 十、总结一句话版

> **GitLab CI = GitLab + Runner + `.gitlab-ci.yml`**
> Runner 是肌肉，CI 文件是神经，Docker 是骨骼 🦾

------

如果你愿意，我可以继续帮你做下面任意一个：

- 🚀 一份 **标准企业级 `.gitlab-ci.yml` 模板**
- 🐳 Docker 镜像构建 + 推送流水线
- ☸️ CI 自动发布到 Kubernetes
- 🧠 CI 常见报错“对照表”

你想先啃哪一块？