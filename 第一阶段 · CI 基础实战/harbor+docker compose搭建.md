好，我们来把 **Harbor 用 Docker 正式搭起来**。这是一套偏生产的流程，步骤多一点，但每一步都踏实。Harbor 像一个港口，Docker 镜像的船都在这里靠岸 ⚓。

下面以 **Docker + docker-compose（Harbor 官方方式）** 为例。

------

## 一、Harbor 架构先过一眼

Harbor 不是一个单容器，而是一组协作的服务：

- **harbor-core**：核心 API
- **harbor-registry**：Docker Registry
- **harbor-db**：数据库
- **harbor-redis**：缓存
- **harbor-portal**：Web UI
- **nginx**：统一入口

所以它 **必须用 docker-compose 或 Kubernetes**。

------

## 二、环境要求

### 1️⃣ 机器最低配置（建议）

| 资源 | 建议                             |
| ---- | -------------------------------- |
| CPU  | 2 核                             |
| 内存 | 4 GB（推荐 8GB）                 |
| 磁盘 | ≥ 40 GB                          |
| OS   | Linux（CentOS / Rocky / Ubuntu） |

------

### 2️⃣ 必备软件

```bash
docker --version        # >= 20.x
docker-compose --version # >= 1.25
```

------

## 三、下载安装 Harbor 安装包

### 1️⃣ 下载官方离线包（推荐）

```bash
wget https://github.com/goharbor/harbor/releases/download/v2.9.4/harbor-offline-installer-v2.9.4.tgz
```

（版本可按需调整）

### 2️⃣ 解压

```bash
tar xf harbor-offline-installer-v2.9.4.tgz
cd harbor
```

目录里你会看到：

```
harbor.yml.tmpl
prepare
install.sh
```

------

## 四、配置 Harbor（关键）

### 1️⃣ 复制配置文件

```bash
cp harbor.yml.tmpl harbor.yml
```

------

### 2️⃣ 编辑 `harbor.yml`

```bash
vim harbor.yml
```

### 最小可用配置示例（HTTP）

```yaml
hostname: harbor.local

http:
  port: 80

harbor_admin_password: Harbor12345

database:
  password: root123
  max_idle_conns: 50
  max_open_conns: 200

data_volume: /data/harbor
```

#### 关键说明

| 配置项                | 说明                    |
| --------------------- | ----------------------- |
| hostname              | 访问 Harbor 的域名或 IP |
| harbor_admin_password | admin 初始密码          |
| data_volume           | 镜像、数据库的存储路径  |

⚠️ `hostname` 必须和你 docker login 用的一致。

------

## 五、准备目录（必须）

```bash
mkdir -p /data/harbor
```

建议权限：

```bash
chown -R root:root /data/harbor
```

------

## 六、安装 Harbor

### 1️⃣ 执行安装脚本

```bash
./install.sh
```

看到类似输出说明成功：

```
✔ ----Harbor has been installed and started successfully.----
```

------

### 2️⃣ 查看容器状态

```bash
docker ps
```

你会看到一堆 `harbor-*` 容器在运行。

------

## 七、访问 Harbor Web

浏览器访问：

```
http://<hostname>
```

登录：

- 用户名：`admin`
- 密码：`harbor_admin_password` 中配置的

------

## 八、Docker 客户端对接 Harbor

### 1️⃣ 如果是 HTTP Harbor（重要）

Docker 默认 **不信任 HTTP Registry**，需要配置。

#### 编辑 Docker 配置：

```bash
vim /etc/docker/daemon.json
{
  "insecure-registries": ["harbor.local"]
}
```

重启 Docker：

```bash
systemctl restart docker
```

------

### 2️⃣ 登录 Harbor

```bash
docker login harbor.local
```

------

### 3️⃣ 推送镜像测试

```bash
docker tag nginx:1.25 harbor.local/library/nginx:1.25
docker push harbor.local/library/nginx:1.25
```

Web 页面能看到镜像，说明 Harbor 跑通了。

------

## 九、Harbor + GitLab CI（常见搭配）

CI 中登录 Harbor：

```yaml
before_script:
  - docker login harbor.local -u admin -p Harbor12345
```

构建并推送：

```yaml
script:
  - docker build -t harbor.local/app/demo:$CI_COMMIT_SHA .
  - docker push harbor.local/app/demo:$CI_COMMIT_SHA
```

------

## 十、生产环境必做清单（很重要）

- ✅ 换 HTTPS（Let’s Encrypt / 自签 CA）
- ✅ 修改 admin 密码
- ✅ 开启项目配额
- ✅ 镜像扫描（Trivy）
- ✅ 定期备份 `/data/harbor`

------

## 十一、一句话总结

> **Harbor = 企业级 Docker 镜像仓库 + 权限 + 安全 + UI**
> GitLab 管代码，Harbor 管镜像，它们是 DevOps 的左右手 🤝

------

如果你愿意，我可以继续帮你：

- 🔐 配置 **Harbor HTTPS（自签 / CA）**
- 🔁 **GitLab CI 自动构建并推送 Harbor**
- 🧠 Harbor 常见坑位（证书 / 登录 / push 失败）
- ☸️ Harbor 部署到 Kubernetes

你想从哪一步继续？