好，咱们把 **Git 从 0 到 1** 做成一套「**真·敲命令**」的实操闯关本。
不是讲概念，是一路打怪升级，敲完你就会 

------

#  Git 从 0 到 1 · 实操练习题（循序渐进）

> 目标：
>
> - 看懂 Git 在“干嘛”
> - 敢在真实项目里用
> - 不再怕 `reset / rebase / merge`

------

##  第 0 关：准备工作（5 分钟）

### 练习 0-1：检查环境

```bash
git --version

$ git --version
git version 2.51.0.windows.1

```

### 练习 0-2：配置身份（只做一次）

```bash
git config --global user.name "YourName"
git config --global user.email "you@example.com"
```

✔️ 验证：

```bash
git config --global --list
```

------

##  第 1 关：本地仓库的诞生

### 练习 1-1：创建仓库

```bash
mkdir git-lab
cd git-lab
git init
```

观察：

```bash
ls -a
```

❓思考：`.git` 是什么？删了会怎样？

------

### 练习 1-2：第一次提交

```bash
echo "Hello Git" > readme.txt
git status
git add readme.txt
git commit -m "first commit"
```

✔️ 验证：

```bash
git log
```

 理解关键词：

- 工作区
- 暂存区
- 仓库

------

##  第 2 关：反复修改与提交

### 练习 2-1：多次提交

```bash
echo "line 2" >> readme.txt
git status
git diff
git add .
git commit -m "add second line"
```

再来一次：

```bash
echo "line 3" >> readme.txt
git commit -am "add third line"
```

❓思考：

- `git add .` vs `git commit -am`
- 哪种文件不能用 `-am`？

------

##  第 3 关：后悔药（回滚）

### 练习 3-1：撤销工作区修改

```bash
echo "wrong line" >> readme.txt
git checkout -- readme.txt
```

------

### 练习 3-2：撤销暂存区

```bash
echo "test" >> readme.txt
git add readme.txt
git reset HEAD readme.txt
```

------

### 练习 3-3：回退提交（重点）

```bash
git log --oneline
git reset --soft HEAD~1
git reset --mixed HEAD~1
git reset --hard HEAD~1
```

⚠️ 体会三种 reset 的区别（这是 Git 的分水岭）

------

##  第 4 关：分支就是平行宇宙

### 练习 4-1：创建并切换分支

```bash
git branch dev
git checkout dev
```

或：

```bash
git switch -c dev
```

------

### 练习 4-2：分支提交

```bash
echo "dev work" > dev.txt
git add .
git commit -m "dev commit"
```

------

### 练习 4-3：合并分支

```bash
git checkout master
git merge dev
```

✔️ 验证：

```bash
git log --oneline --graph
```

------

##  第 5 关：冲突现场（必练）

### 练习 5-1：制造冲突

master 分支：

```bash
echo "master change" > conflict.txt
git add .
git commit -m "master change"
```

dev 分支：

```bash
git checkout dev
echo "dev change" > conflict.txt
git add .
git commit -m "dev change"
```

合并：

```bash
git checkout master
git merge dev
```

 出现冲突

------

### 练习 5-2：解决冲突

```bash
vim conflict.txt
git add conflict.txt
git commit
```

🧠核心认知：
**Git 不会帮你选，它只负责提醒**

------

## 第 6 关：远程仓库（GitHub）

### 练习 6-1：关联远程仓库

```bash
git remote add origin https://github.com/xxx/git-lab.git
git branch -M main
git push -u origin main
```

------

### 练习 6-2：拉取与推送

```bash
git pull
git push
```

------

## 第 7 关：克隆与协作

### 练习 7-1：克隆仓库

```bash
git clone https://github.com/xxx/git-lab.git
```

------

### 练习 7-2：模拟团队协作

- 本地修改
- push
- 另一端修改
- pull 产生冲突并解决

------

## 第 8 关：高级但常用

### 练习 8-1：stash

```bash
git stash
git stash list
git stash pop
```

------

### 练习 8-2：rebase（慎用但必会）

```bash
git checkout dev
git rebase main
```

理解：

- rebase 改历史
- merge 保留历史

------

## 终极实战任务（毕业题）

目标：模拟真实 DevOps 场景**

1. main 为稳定分支
2. dev 为开发分支
3. feature/login 为功能分支
4. feature 完成 → 合并 dev
5. dev 测试通过 → 合并 main
6. main 打 tag 发布

```bash
git tag v1.0
git push origin v1.0
```

------

##  学完你应该做到

✅ 看 `git status` 就知道下一步
✅ 冲突不慌
✅ 知道什么时候用 reset / revert
✅ 能和 CI/CD、K8s 项目无缝配合

------

如果你愿意，我可以下一步直接给你：

-  **7 天 Git 强化实战表**
-  **Git 面试高频题（运维 / DevOps）**
-  **真实团队 Git 工作流演练（PR / Review / Rebase）**

你选哪条路线？