
# **Git 实战练习手册：个人博客项目案例**

## **阶段 0：准备环境**

1. 安装 Git：

```bash
git --version
# 如果没有安装，去官网下载安装 https://git-scm.com/
```

2. 配置用户名和邮箱：

```bash
git config --global user.name "YourName"
git config --global user.email "you@example.com"
```

3. 检查配置：

```bash
git config --list
```

✅ **目标**：Git 环境准备完毕。

---

## **阶段 1：初始化项目**

```bash
mkdir my-blog
cd my-blog
git init
echo "# My Blog" > README.md
git add README.md
git commit -m "初始化项目，添加 README"
```

* **命令解析**：

  * `git init` → 初始化本地仓库
  * `git add` → 添加文件到暂存区
  * `git commit` → 提交到本地仓库

✅ **目标**：掌握 Git 基础操作。

---

## **阶段 2：远程仓库**

1. 在 GitLab 或 GitHub 创建仓库 `my-blog`
2. 关联远程：

```bash
git remote add origin <仓库地址>
git branch -M main
git push -u origin main
```

✅ **目标**：熟悉远程仓库操作，理解 `push` 与 `pull`。

---

## **阶段 3：分支管理**

### 创建和切换分支

```bash
git checkout -b feature/header
git checkout main
git checkout -b feature/footer
```

### 在分支上开发

```bash
# feature/header
echo "<header>我的博客</header>" > header.html
git add .
git commit -m "添加网站头部"

# feature/footer
echo "<footer>版权信息</footer>" > footer.html
git add .
git commit -m "添加网站底部"
```

### 推送到远程

```bash
git push -u origin feature/header
git push -u origin feature/footer
```

✅ **目标**：掌握分支创建、切换、提交和远程操作。

---

## **阶段 4：合并与冲突**

### 合并分支

```bash
git checkout main
git merge feature/header
git merge feature/footer
```

### 模拟冲突

```bash
# feature/header
echo "<h1>博客标题</h1>" > index.html
git commit -am "header 修改 index.html"

# feature/footer
echo "<h2>博客副标题</h2>" > index.html
git commit -am "footer 修改 index.html"

# 合并会冲突
git checkout main
git merge feature/footer
# 手动编辑冲突文件
git add index.html
git commit -m "解决冲突"
```

✅ **目标**：学习冲突发现与解决。

---

## **阶段 5：查看历史和回退**

### 查看提交历史

```bash
git log --oneline --graph --all
```

### 回退

```bash
# 回退到上一个提交
git reset --hard HEAD~1
```

✅ **目标**：掌握历史查看和回退操作。

---

## **阶段 6：临时存储（stash）**

```bash
# 修改文件但不提交
echo "临时修改" >> README.md

# 存入 stash
git stash

# 查看 stash
git stash list

# 恢复 stash
git stash pop
```

✅ **目标**：学会临时保存未完成的修改。

---

## **阶段 7：整理提交（rebase）**

```bash
git checkout feature/header
git rebase main
# 如果冲突，解决后 git rebase --continue
```

✅ **目标**：掌握 rebase 和整理提交记录。

---

## **阶段 8：清理分支**

```bash
# 删除本地已合并分支
git branch -d feature/header
git branch -d feature/footer

# 删除远程分支
git push origin --delete feature/header
git push origin --delete feature/footer
```

✅ **目标**：学会分支管理和清理。

---

## **阶段 9：拓展练习**

1. 添加 `.gitignore` 忽略日志或临时文件
2. 尝试 `git cherry-pick` 拿单个提交到其他分支
3. 尝试 `git revert` 撤销历史提交
4. 使用 `git tag` 标记版本
5. 用 `git diff` 查看修改前后差异

---

这个手册设计成 **练习路线图**，每一步都是实际操作场景，可以边做边记命令、掌握 Git 核心流程。

如果你想，我可以帮你做一个 **图形化 Git 操作流程图**，把 **分支、合并、冲突、回退、stash、rebase** 用图画出来，一眼就能看明白整个流程。

你想要我画吗？
