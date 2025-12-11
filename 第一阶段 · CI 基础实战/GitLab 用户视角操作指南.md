# *GitLab 用户视角操作指**
>管理员的世界像机房，而用户的世界更像一块温顺的画布，你只管在上面写代码、建项目、提 MR、跑流水线

>我只讲**普通用户能做的事**，一步步、可直接照做


# 一、登录与修改个人信息

 **1. 登录**
管理员会给你：

* 登录地址
* 用户名
* 密码（或邮箱激活链接）

登录后，你会看到 GitLab 的主界面。

 **2. 修改密码 / SSH Key**
右上角头像
→ **Edit Profile**

你可以：

* 修改密码
* 添加 SSH Key（推荐用 SSH clone）

SSH key 在这里添加：
**Preferences** → **SSH Keys**



# 二、加入项目（由管理员邀请）

用户无法自行加入项目，要等待管理员或项目维护者邀请。

收到邀请后：

* 会出现在你的“**Projects → Your Projects**”里
* 或者你会收到邮件通知

进入项目后，你就能进行所有开发相关操作。



# 三、克隆项目到本地

项目页面右上角有 Clone 按钮。

支持两种方式：

 **SSH 克隆（推荐）**

```bash
git clone git@gitlab.example.com:group/project.git
```

 **HTTP 克隆（需要输入账号密码）**

```bash
git clone https://gitlab.example.com/group/project.git
```


# 四、日常开发流程（用户最核心的操作）

这就是用户的日常呼吸节奏。

## 1) 创建分支

```bash
git checkout -b feature/my-new-change
```

## 2) 编写代码并提交

```bash
git add .
git commit -m "实现新功能"
```

## 3) 推送代码

```bash
git push origin feature/my-new-change
```


# 五、发起 Merge Request（用户最常用动作之一）

代码推上去后，在 GitLab 中：

左侧菜单
→ **Merge Requests**
→ **New Merge Request**

选择：

* Source branch：你的 feature 分支
* Target branch：一般是 `main` 或 `develop`

填写标题、描述
点击 **Create Merge Request**

MR 就会进入代码审核流程。


# 六、查看 Pipeline（CI/CD）

在项目左侧：

→ **CI/CD**
→ **Pipelines**

你能看到：

* 是否构建成功
* 测试是否通过
* 构建的日志
* 产物 Artifacts

用户无需配置，只需要关注结果。


# 七、提交 Issue（相当于“问题与任务”）

左侧菜单
→ **Issues**
→ **New Issue**

常见用法：

* 记录 bug
* 提需求
* 任务分配
* 项目管理

可以选择 assignee（负责人）和 label（标签）。


# 八、查看并使用 Wiki（项目文档）

如果项目开启了 Wiki，你可以作为用户：

* 创建文档
* 编辑项目知识库
* 写技术说明、使用指南等

路径：左侧菜单 → **Wiki**


# 九、用户能做的权限范围

你的权限由项目管理员决定：

* **Reporter**：只能看
* **Developer**：能 push、能提 MR
* **Maintainer**：能合并 MR、能管理 CI/CD 配置


#  最后，为你总结成一句话

**用户的世界只围绕四个动作旋转：Clone、Commit、Push、Merge。**
其他都是锦上添花。


如果你愿意，我可以给你整理一份更短的：

### ✔ 一页版《GitLab 用户使用速查表》

或

### ✔ GitLab 用户操作流程图（图形版）

你想要哪一种？
