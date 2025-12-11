管理员在 GitLab 里，就像掌握整座“代码城邦”钥匙的人。城墙、道路、护卫、仓库、流水线，全由他来设置。下面我给你一份**“GitLab 管理员能做的所有事”全景图**，结构干净、可当日常参考。

---

# 🏰 一、用户管理：掌控人口与身份

### 1. 创建/删除用户

Admin Area → **Users**

* 创建用户
* 激活/禁用
* 强制重置密码

### 2. 管理用户权限

* 设置为普通用户或管理员
* 调整访问级别
* 限制登录方式

### 3. 强制两步验证、限制密码强度

帮团队筑起安全外墙。

### 4. 查看用户活动记录

谁登录、谁 push、谁删库，全都能看到。

---

# 🗂 二、Group 管理：搭建部门结构

管理员可以：

* 创建顶级组（Group）
* 管理子组
* 设定组级别权限
* 控制 group 下的所有项目模板、CI 模板

Group 就像 GitLab 的行政区，项目住在里面。

---

# 📦 三、项目管理：掌控仓库的一切

### 管理员能：

* 创建/删除项目
* 修改项目可见性（Private/Internal/Public）
* 给项目强制启用/关闭功能

  * Issue
  * MR
  * Wiki
  * Pipeline
  * Container Registry
  * Package Registry

### 可以强制设置：

* 默认分支
* 分支保护
* 强制 MR 审核规则（例如必须 2 人 approve）
* 限制谁能 push、谁能 merge

---

# 🤖 四、CI/CD 与 Runner 管理：流水线的发动机房

### 1. 注册与管理 GitLab Runner

管理员可以：

* 配置 **shared runner**（全局可用）
* 控制 runner 的并发数
* 设定 runner 标签
* 限制某些 projects 使用 runner

### 2. CI/CD 安全策略

管理员可为整个实例定义：

* 变量保密规则
* 受保护变量
* 跨项目 pipeline 规则

像把整套工厂的“安全手册”写好。

---

# 🔐 五、安全与合规：建城墙、挂告示

管理员能配置：

### 安全策略

* SSH key 长度
* 账号锁定策略
* 密码复杂度
* 审计日志 retention
* 审批策略（MR 要几人签字）

### 合规设置

* 创建流水线审批
* 合规规则文件（Compliance Pipeline）
* 审计日志导出

---

# 🔔 六、系统级设置：GitLab 整个宇宙的天条

Admin Area → Settings

管理员可管理：

### General

* 限制可见性
* 项目、用户默认设置
* 允许/禁止注册用户

### Network

* 保护 IP
* 限制 outbound 请求
* 配置 Webhook 访问白名单

### Integrations

* SMTP（邮件）
* OAuth/LDAP/企业 SSO
* Prometheus
* Slack/Teams

### Appearance

* Logo
* 欢迎信息
* Banner 通知

---

# 🗃 七、存储与备份：整个城市的地基

管理员负责：

### 仓库存储

* Repository 存储路径
* Artifacts / Packages / LFS 存储

### 备份与恢复

* gitlab-backup create
* gitlab-backup restore

### 清理规则

* 清理旧 artifacts
* 清理旧 MR
* 清理容器镜像

---

# 📡 八、监控与运维：监听引擎温度

管理员能访问：

* 实例级 Metrics
* Runner 健康状态
* Sidekiq 队列
* Prometheus 集成
* Grafana dashboard（如你使用 Omnibus）

---

# 🧨 九、危机处理：管理员的“红色按钮”

管理员具备最高权限，可以：

* **阻止某用户 push**
* **封禁账号**
* **恢复误删项目（Soft delete）**
* **紧急修改 Runner Key**
* **删库**
* **强制创建/合并分支**

红色按钮不常按，但按的时候就是救火现场。

---

# 🌕 十、总结成一句话

**管理员控制整个 GitLab 的“基础设施、安全、权限、项目体系和流水线引擎”，是维护城市平稳运行的人。**

---

如果你愿意，我可以继续给你做一份：

### ✔ GitLab 管理员职责 SOP

或

### ✔ GitLab 管理员 vs 用户 权限对比表

或

### ✔ 私有 GitLab 管理最佳实践（升级、备份、Runner 管理、监控）

告诉我你想哪一种，我马上为你织出来。


下面这份是给“私有 GitLab 管理者”的**长期护城河指南**，像一本稳重却带点呼吸感的《城池运维手册》。不走花架子，全部是经得住日常折腾与线上事故的实践经验。

---

# 🌕 一、部署方式的选择：地基要稳

你的 GitLab 城堡由两种砖块组成：

## 1) Omnibus（推荐大多数团队）

一体化、升级轻松、官方支持强。
适合：中型团队、追求稳定性。

## 2) GitLab Helm Chart（Kubernetes）

集群化、可扩展、自动恢复强。
适合：大型团队、有 DevOps 团队的企业。

无论你选哪种，原则只有一句：
**先稳，再快。**

---

# 🌲 二、版本管理策略：永远不要跳两级升级

GitLab 的升级像登山，一级一级走，不要跨越山脊。

最佳实践：

* 每 1~2 个月 **小版本** 更新一次（安全补丁）
* 每半年 **大版本** 更新一次
* 切记：**不要跨越超过 1 个 major 版本升级**
* 升级前执行 `gitlab-backup`
* 升级后检查 Sidekiq、Runner 状态
* 高峰期永不升级

升级顺序是：

```
X.Y.Z → X.(Y+1).0 → X.(Y+1).1 → ... → X.(Y+2).0
```

别贪快，这条规矩能让你少掉很多的深夜。

---

# 🗃 三、备份策略：像钟表一样规律

GitLab 的备份应像呼吸一样自动发生。

## 1) 每日一次备份

```bash
gitlab-backup create
```

## 2) 备份内容包含

* 仓库（Git）
* LFS + Artifacts
* CI/CD 产物
* Wiki
* Registry（可独立备份）
* 数据库

## 3) 备份策略

* 只保留最近 14 或 30 天
* 本地存一份
* 远程 OSS/S3 再存一份
* 必须定期做一次 **恢复演练**

恢复不演练 = 不存在的备份。

---

# 📦 四、Runner 管理：流水线引擎的氧气供应

## 必做：

✔ 使用 **Shared Runner + Project Runner** 双轨制
✔ 编写 Runner “黄金参数模板”
✔ 用 autoscaler（K8s、ECS、GCP、AWS）让 Runner 按需扩缩
✔ Runner 严禁使用管理员 Token（泄漏就炸）
✔ 为 Runner 设置 CPU/MEM 限额，避免它吃光宿主机

## 不要做：

✘ 不要让 Runner 和 GitLab 同机部署
✘ 不要让所有项目共用一个 Runner Token
✘ 不要让 CI Job 访问本机 127.0.0.1（你以为的 localhost 不一定是你想的那台）

---

# 🔐 五、安全策略：把城墙砌牢

## 1) 强制 SSH Key 长度 ≥ 4096

## 2) 禁止普通用户创建项目（由管理员控制）

## 3) 默认项目可见性设为 Private

## 4) 强制开启 2FA（二步验证）

## 5) 至少一个管理员账号安全隔离保存

## 6) MR merge 必须至少 1 人审核

## 7) 防止“删库跑路”：

* 禁止普通用户删除项目
* 开启“Delayed Delete”
* 管理员定期导出 audit log

---

# 🔧 六、性能与存储：让 GitLab 呼吸通畅

## 1) Gitaly（Git 存储后端）

* SSD，不要 HDD
* IOPS 足够高，否则 push 会像冬天的老铁门
* 如果是大企业：部署 Gitaly Cluster

## 2) PostgreSQL 配置

* 使用外部 PostgreSQL 时，开启高可用（HA）
* 内置数据库使用默认参数即可，但要定期 vacuum

## 3) Object Storage 存储

强烈建议将 Artifacts / LFS / Registry 放 OSS / S3，不要把 GitLab 服务器当拖拉机。

---

# ⛲ 七、清理规则：给系统减负

GitLab 会默默囤积各种“历史尘埃”，你要定期打扫：

## 1) CI Job Artifacts 清理

```bash
gitlab-rake gitlab:cleanup:orphan_artifacts
```

## 2) Registry 清理

支持 Tag 保护策略和 TTL 策略。

## 3) LFS 清理

```bash
gitlab-rake gitlab:lfs:clean
```

## 4) MR、Pipeline 历史清理

设置过期时间即可自动执行。

---

# 📡 八、监控：让系统脉搏可视化

推荐开启：

### 必开监控：

* Prometheus（内置）
* Grafana（外部）
* Sidekiq 队列监控
* Runner 健康度

### 核心监控指标：

* Sidekiq backlog
* Runner queue duration
* Gitaly latency
* PostgreSQL connection count
* 磁盘占用率
* Redis 连接数

一个健康的 GitLab 像心率稳定的长跑者。

---

# 🧨 九、应急响应：管理员的刀锋时刻

当 GitLab 出现红灯：

## 1) GitLab 无响应

```bash
gitlab-ctl status
gitlab-ctl restart
```

## 2) PostgreSQL 爆满

紧急 vacuum
扩容磁盘
迁移到外部数据库

## 3) 仓库损坏

使用 GitLab 的 “Repo Housekeeping” 修复

## 4) Runner 全死

检查 Token
检查 Docker/K8s 节点资源
重建 Runner

## 5) 用户误删项目

到 Admin 自助恢复区找回
或从备份恢复（你提前练习过的那种）

---

# 🌤 十、管理员日常 SOP（可贴到墙上）

每天：

* 看 Sidekiq、Runner 监控图

每周：

* 清理老 artifacts、registry
* 回顾失败 pipeline 原因（统筹优化）

每月：

* 小版本升级
* 检查备份是否可恢复

每半年：

* 大版本升级
* 全面安全检查（用户权限、过期账号）

---

# 🎇 最后一句

**私有 GitLab 管理不是“守城”，而是让整个研发体系像城市供电一样稳定运行。**

---

如果你愿意，我可以进一步提供：

### ✔ GitLab 私有化部署架构图（K8s + Runner + Storage）

### ✔ GitLab 管理员月度巡检清单（可打印）

### ✔ GitLab 故障排查流程图（红色按钮版）

你要哪一个？
