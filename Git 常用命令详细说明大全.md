下面给你一份**Git 常用命令详细说明大全**，我会按「真实工作流」来讲，而不是命令说明书式的堆砌。把 Git 想成一条流水线，代码在不同“站台”来回切换 🧭

---

## 一、Git 三大核心区域（先立世界观）

在讲命令前，先认清 Git 的三层结构：

```
工作区（Working Directory） → 暂存区（Stage / Index） → 仓库（Repository）
```

* **工作区**：你正在编辑的文件
* **暂存区**：即将提交的“候选区”
* **仓库**：已经提交、写入历史的版本

👉 大部分 Git 命令，本质就是在“搬文件”

---

## 二、初始化 & 克隆

### 1️⃣ 初始化仓库

```bash
git init
```

* 把当前目录变成 Git 仓库
* 生成 `.git/` 隐藏目录
* 常用于新项目

📌 场景：从零开始一个项目

---

### 2️⃣ 克隆远程仓库

```bash
git clone https://github.com/xxx/xxx.git
```

* 拉取完整代码 + 历史记录
* 默认会配置好 `origin` 远程仓库

📌 场景：接手已有项目

---

## 三、查看状态 & 差异（最常用）

### 3️⃣ 查看当前状态（高频）

```bash
git status
```

告诉你三件事：

* 哪些文件被修改了
* 哪些在暂存区
* 哪些还没被 Git 管理

🧠 建议：**每次提交前必看**

---

### 4️⃣ 查看文件差异

```bash
git diff
```

* 工作区 vs 暂存区

```bash
git diff --cached
```

* 暂存区 vs 上一次提交

📌 场景：提交前确认改了啥

---

## 四、添加 & 提交（核心动作）

### 5️⃣ 添加到暂存区

```bash
git add file.txt
```

```bash
git add .
```

* `.` 表示当前目录所有修改

⚠️ 注意：`git add` 不是提交，只是“选中”

---

### 6️⃣ 提交到本地仓库

```bash
git commit -m "fix: 修复登录超时问题"
```

* 真正写入历史
* `-m` 是提交说明

📌 好的提交信息：

```
feat: 新增用户注册
fix: 修复空指针异常
docs: 更新 README
```

---

## 五、查看历史 & 版本穿梭

### 7️⃣ 查看提交历史

```bash
git log
```

常用简化版：

```bash
git log --oneline --graph --decorate
```

像一棵时间树 🌳

---

### 8️⃣ 回到某个版本（不推荐直接用）

```bash
git checkout commit_id
```

📌 会进入“游离 HEAD”状态
👉 一般用于查看历史，不用于开发

---

## 六、撤销操作（救命区）

### 9️⃣ 撤销工作区修改（未 add）

```bash
git checkout -- file.txt
```

或新命令：

```bash
git restore file.txt
```

⚠️ 改动直接消失，慎用

---

### 🔟 撤销暂存区（已 add，未 commit）

```bash
git reset HEAD file.txt
```

或：

```bash
git restore --staged file.txt
```

---

### 1️⃣1️⃣ 撤销最近一次提交（未 push）

```bash
git reset --soft HEAD~1
```

* 提交没了
* 代码还在暂存区

```bash
git reset --hard HEAD~1
```

* 提交没了
* 代码也没了 💀

---

## 七、分支操作（团队协作核心）

### 1️⃣2️⃣ 查看分支

```bash
git branch
```

---

### 1️⃣3️⃣ 创建分支

```bash
git branch dev
```

---

### 1️⃣4️⃣ 切换分支

```bash
git checkout dev
```

或新写法：

```bash
git switch dev
```

---

### 1️⃣5️⃣ 创建并切换

```bash
git checkout -b feature/login
```

---

### 1️⃣6️⃣ 合并分支

```bash
git merge dev
```

📌 场景：把 dev 合并到当前分支

---

## 八、远程仓库（GitLab / GitHub）

### 1️⃣7️⃣ 查看远程仓库

```bash
git remote -v
```

---

### 1️⃣8️⃣ 拉取远程更新

```bash
git pull
```

= `git fetch` + `git merge`

---

### 1️⃣9️⃣ 推送代码

```bash
git push origin main
```

📌 第一次推送：

```bash
git push -u origin main
```

---

## 九、真实生产常用组合（重点）

### 日常开发标准流程

```bash
git pull
git status
git add .
git commit -m "feat: xxx"
git push
```

---

### 修改提交说明（未 push）

```bash
git commit --amend
```

---

### 查看是谁改的（甩锅神器）

```bash
git blame file.txt
```

---

## 十、Git 命令地图（记忆版）

```
写代码 → git status
选代码 → git add
存历史 → git commit
看历史 → git log
拉更新 → git pull
推代码 → git push
```

---

如果你愿意，我可以下一步直接给你：

* ✅ **Git 生产常用场景实战（冲突、回滚、误删恢复）**
* ✅ **Git + GitLab CI 的完整流水线视角**
* ✅ **运维 / 开发必会的 Git 命令最小集**

你想继续哪一条？

这条命令看起来短，背后却是一次**身份绑定 + 首次发布**。我们把它像解剖钟表一样拆开 ⏱️

---

## 命令本身

```bash
git push -u origin main
```

---

## 一、逐词拆解

### 1️⃣ `git push`

**把本地提交送到远程仓库**

* 推送的是 commit，不是文件
* 远程仓库由 `remote` 决定

---

### 2️⃣ `origin`

**远程仓库的别名**

* 指向你之前配置的 GitLab 仓库地址
* 本质只是一个“书签名”

可以验证：

```bash
git remote -v
```

---

### 3️⃣ `main`

**你要推送的本地分支**

* 当前分支通常也是 `main`
* 如果本地还叫 `master`，这里会直接失败

---

### 4️⃣ `-u`（真正的灵魂）

`-u` = `--set-upstream`

它做了两件事：

1. 在远程创建（或更新）`origin/main`
2. 建立**跟踪关系**

```text
本地 main  ←→  远程 origin/main
```

---

## 二、为什么第一次一定要加 `-u`

没有 `-u` 的世界：

```bash
git push origin main
git pull origin main
```

每次都要写全名，像每次寄信都手写完整地址 📨

有了 `-u` 之后：

```bash
git push
git pull
```

Git 会自动知道：

> “你说的就是 origin/main”

---

## 三、执行后 Git 内部发生了什么

### 1️⃣ 远程发生变化

* GitLab 上出现分支 `main`
* 包含你本地所有提交

### 2️⃣ 本地发生变化

* `.git/config` 多了一段：

```ini
[branch "main"]
    remote = origin
    merge = refs/heads/main
```

这就是“绑定关系”的证据。

---

## 四、什么时候会失败（真实踩坑）

### ❌ 情况 1：还没有 commit

报错：

```text
error: src refspec main does not match any
```

原因：

* `main` 分支没有任何提交

解决：

```bash
git commit -m "init"
```

---

### ❌ 情况 2：远程仓库还没创建

报错：

```text
repository not found
```

原因：

* GitLab 项目不存在
* 或你没权限

---

### ❌ 情况 3：远程已存在不同历史

报错：

```text
rejected: non-fast-forward
```

原因：

* 远程仓库已经有 README / LICENSE
* 本地历史对不上

解决（首次）：

```bash
git pull --rebase origin main
git push -u origin main
```

---

## 五、这条命令在 CI/CD 中的意义

对 GitLab CI 来说：

> **第一次 `git push -u origin main`
> = 项目“正式上线”的信号**

之后：

* 每一次 `git push`
* 都可能触发：

  * CI 测试
  * Docker 构建
  * 自动部署

---

## 六、一句话总结

> **`git push -u origin main`
> 不是一次普通推送，
> 而是给分支办了长期居住证。**

如果你愿意，下一步我可以直接接着讲：

* 🔒 如何把 `main` 设成**保护分支**
* 🚦 CI 只在 `main` 自动发布，其它分支只跑测试
* 🧩 `.gitlab-ci.yml` 里 `main` 的最佳写法

你想继续哪一段？

