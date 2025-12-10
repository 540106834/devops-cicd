📦 **Git & GitLab：CI 的起点，也是 DevOps 的起跑线**

你当前正站在 CI 的第一块地砖上，而这块砖就叫：**Git + GitLab**。
如果把 CI/CD 想成一条自动化工厂线：

> **Git 是传送带 · GitLab 是数字化车间**

---

# 一句话定乾坤

* ✅ **Git = 版本控制工具**
* ✅ **GitLab = 围绕 Git 的协作与 CI 平台**

---

---

## 🧠 先说人话版

### Git

👉 是一个命令行工具

作用：

* 保存代码版本
* 支持分支开发
* 支持合并回主线
* 支持追溯历史

像给代码装了**时光机**：

```
现在  ← checkout →  半小时前  ← revert →  三周前
```

---

---

### GitLab

👉 是一个 Web 平台 + Git 服务器

作用：

* 提供 Git 仓库地址
* 提供 Web 可视化管理
* 做权限、审计、协作
* **内置 CI/CD**

本质是一整套：

```
仓库服务 + MR + 权限 + 流水线 + 制品库
```

---

---

## ⚙️ 功能拆解对照表

| 能力         | Git | GitLab |
| ---------- | --- | ------ |
| 管理代码版本     | ✅   | ✅      |
| 多分支协作      | ✅   | ✅      |
| 历史回滚       | ✅   | ✅      |
| Web 界面     | ❌   | ✅      |
| 权限管理       | ❌   | ✅      |
| Issue / MR | ❌   | ✅      |
| CI/CD 集成   | ❌   | ✅      |

---

---

## 🏗 用你能感知的工作流描述

一个真实 DevOps 开发日常：

```
写代码
  ↓
git add / git commit
  ↓
git push → GitLab
  ↓
GitLab 自动触发 CI
  ↓
Pipeline 开始构建
```

---

---

## 🛤 最小学习闭环

你现在要掌握的 Git & GitLab 其实只要这一条黄金路线：

```
本地写 → Git提交 → 推GitLab → 触发CI
```

---

---

---

# Git 必会 10 条命令

你掌握这些就可以干活：

```bash
git init               # 初始化仓库
git clone <repo>       # 克隆代码
git status             # 查看状态
git add .              # 加入暂存区
git commit -m "msg"    # 提交
git branch             # 查看分支
git checkout -b dev    # 新建并切换分支
git merge dev          # 合并分支
git pull               # 拉取更新
git push               # 推送到远端
```

---

---

## 🌱 Git 分支模型（企业版）

99% 公司都用这个：

```
master/main  ← 稳定主线
develop      ← 日常联调
feature/*    ← 开发新功能
hotfix/*     ← 紧急修复
```

---

---

## 🚦 GitLab 工作流（典配）

```
feature/* 开发
    ↓
Push 到 GitLab
    ↓
Merge Request (MR)
    ↓
CI 自动构建
    ↓
Review
    ↓
合并到 develop
```

---

---

---

## ⚙️ GitLab CI 基础

只要库里有这个文件：

```yaml
.gitlab-ci.yml
```

GitLab 就会自动跑 CI。

---

### 🔹 最简单流水线示例：

```yaml
stages:
  - build
  - test

build_job:
  stage: build
  script:
    - echo "Build ..."

test_job:
  stage: test
  script:
    - echo "Test ..."
```

---

效果：

```
git push → GitLab → CI自动跑
```

---

---

---

## 🔗 GitLab Runner 是啥？

你可以理解为：

> **Runner = 能实际执行流水线任务的“工人节点”**

---

执行关系：

```
GitLab → 派任务 → Runner → 执行脚本
```

常见部署方式：

```bash
docker run gitlab/gitlab-runner
```

---

---

---

## 🪛 你 CI 第一次完整拼图

你现在真实要玩的完整链路👇

```
写代码
   ↓
git commit
   ↓
git push 
   ↓
GitLab 接收
   ↓
.gitlab-ci.yml 生效
   ↓
Runner 执行
   ↓
Docker 构建
```

---

---

---

## 🎯 你这阶段的毕业标准

如果你能做到：

✅ 能用 Git 多分支开发
✅ 能创建 GitLab 仓库并 push 代码
✅ 能写 `.gitlab-ci.yml` 触发流水线
✅ 能看懂 Runner 执行日志

——那你就已经是真正**迈入 CI 工程师门槛**了 ✅

---

---

---

## 🧭 下一步实操建议

你距离“跑通人生第一条 CI 流水线”只差 3 步：

---

### Step 1

确认你本地已装 Git：

```bash
git --version
```

---

### Step 2

注册一个 GitLab 帐号（或部署私有 GitLab）

---

### Step 3

跑这条最小流水线：

```yaml
hello:
  script:
    - echo "Hello CI From GitLab!"
```

---

---

---

## 🚀 接下来你可以选

继续深挖哪块？

👉 **GitLab Runner 实战搭建**
👉 **Git 多分支工作流模拟**
👉 **GitLab CI + Docker 实战**

你挑一个方向，我陪你一直走到能跑生产级流水线。
