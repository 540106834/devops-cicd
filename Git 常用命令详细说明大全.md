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
