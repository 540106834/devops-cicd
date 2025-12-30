
# **Git 实战练习手册：个人博客项目案例**

## **阶段 0：准备环境**

1. 安装 Git：

```bash
git --version
# 如果没有安装，去官网下载安装 https://git-scm.com/

git branch -m master main
# 把“当前分支”重命名为 main
# -m = move / rename 如果存在就拒绝
# -M = move 强制修改
# 不会丢提交，不会新建历史
```

2. 配置用户名和邮箱：
> Git 的用户名和邮箱不是“登录账号”，而是“提交作者签名”。
```bash
git config --global user.name "YourName"
git config --global user.email "you@example.com"
```

配置的作用范围（非常重要）Git 配置是分层的，像三层玻璃：
>优先级：local > global > system

| 层级         | 作用范围 | 使用场景     |
| ---------- | ---- | -------- |
| `--system` | 整台机器 | 很少用      |
| `--global` | 当前用户 | 最常用      |
| `--local`  | 当前仓库 | 公司 / 多身份 |


3. 检查配置：

```bash
git config --list

$ git config --list
diff.astextplain.textconv=astextplain
filter.lfs.clean=git-lfs clean -- %f
filter.lfs.smudge=git-lfs smudge -- %f
filter.lfs.process=git-lfs filter-process
filter.lfs.required=true
http.sslbackend=schannel
core.autocrlf=true
core.fscache=true
core.symlinks=false
pull.rebase=false
credential.helper=manager
credential.https://dev.azure.com.usehttppath=true
init.defaultbranch=master
http.proxy=socks5://127.0.0.1:1080
https.proxy=socks5://127.0.0.1:1080
user.name=540106834
user.email=shenzhe1222@gmail.com

```

 **目标**：Git 环境准备完毕。

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

 **目标**：掌握 Git 基础操作。

---

## **阶段 2：远程仓库**

1. 在 GitLab 或 GitHub 创建仓库 `my-blog`
2. 关联远程：

```bash
git remote add origin <仓库地址> 
# 给本地仓库添加一个“远程仓库别名”，名字叫 origin，指向某个 URL

git branch -M main
# 把当前分支强制改名成 main

git push -u origin main
# 把本地 main 推送到远程 origin，并把两者绑定为“默认上下游”
# -u = --set-upstream
# 从此以后，你的 git push / git pull 都不用再写参数。

```
>init → branch -M main → remote add → push -u一条完整、零歧义的新仓库起飞流程。
```
git init
git branch -M main
git remote add origin <仓库地址>
git push -u origin main
```

 **目标**：熟悉远程仓库操作，理解 `push` 与 `pull`。

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

$ git push -u origin feature/header
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 331 bytes | 331.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feature/header' on GitHub by visiting:
remote:      https://github.com/540106834/my-blog/pull/new/feature/header
remote:
To github.com:540106834/my-blog.git
 * [new branch]      feature/header -> feature/header
branch 'feature/header' set up to track 'origin/feature/header'.

$ git push -u origin feature/footer
Enumerating objects: 4, done.
Counting objects: 100% (4/4), done.
Delta compression using up to 12 threads
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 330 bytes | 330.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
remote:
remote: Create a pull request for 'feature/footer' on GitHub by visiting:
remote:      https://github.com/540106834/my-blog/pull/new/feature/footer
remote:
To github.com:540106834/my-blog.git
 * [new branch]      feature/footer -> feature/footer
branch 'feature/footer' set up to track 'origin/feature/footer'.

```

 **目标**：掌握分支创建、切换、提交和远程操作。

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

 **目标**：学习冲突发现与解决。

---

## **阶段 5：查看历史和回退**

### 查看提交历史

```bash
$ git log --oneline --graph --all
*   4c748b2 (HEAD -> main) Merge branch 'feature/footer'
|\
| * b1ab309 (origin/feature/footer) 添加网站底部
* | 3aff7b8 (origin/feature/header) 添加网站头部
|/
* 8d2793f (origin/main) 初始化项目，添加README

```

### 回退

```bash
# 回退到上一个提交
git reset --hard HEAD~1
```

 **目标**：掌握历史查看和回退操作。

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

 **目标**：学会临时保存未完成的修改。

---

## **阶段 7：整理提交（rebase）**

```bash
git checkout feature/header
git rebase main
# 如果冲突，解决后 git rebase --continue
```

 **目标**：掌握 rebase 和整理提交记录。

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

 **目标**：学会分支管理和清理。

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
