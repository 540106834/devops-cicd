
#  第一阶段 · CI 入门实战路线

你这一阶段的目标只有一句话：

>  会把 **Git 代码 → 自动构建 → 自动测试 → 生成 Docker 镜像**


##  CI 全流程

```
开发提交代码
   ↓
Git 仓库
   ↓
CI 触发
   ↓
拉代码
   ↓
编译 + 单测
   ↓
构建 Docker 镜像
   ↓
推送到镜像仓库
```


##  学习分成 4 块拼图

###  拼图 ①：Git（触发源头）

你要掌握：

```bash
git clone
git pull
git commit
git push
git branch
git merge
```

**核心认知：**

* CI 必须依赖代码提交触发
* 任何 CI 流水线 = 对 Git 事件的自动响应

---

###  拼图 ②：Jenkins（CI 引擎）

你要掌握：

* Jenkins 安装
* 创建流水线 Job
* 写 Jenkinsfile

**Pipeline 基础结构：**

```groovy
pipeline {
  agent any

  stages {
    stage('Checkout') {
      steps {
        git 'https://xxx/hello.git'
      }
    }

    stage('Build') {
      steps {
        sh 'mvn package'
      }
    }

    stage('Test') {
      steps {
        sh 'mvn test'
      }
    }

    stage('Docker') {
      steps {
        sh 'docker build -t demo:v1 .'
      }
    }
  }
}
```


###  拼图 ③：Docker 构建

你要掌握：

```Dockerfile
FROM python:3.11-slim
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["python","main.py"]
```

本质：

> CI 构建出来的终态物必须是：
>  Docker 镜像



###  拼图 ④：镜像仓库

你要学会：

```bash
docker login
docker tag demo:v1 myrepo/demo:v1
docker push myrepo/demo:v1
```

仓库：

* Harbor（私有）
* 阿里 ACR
* Docker Hub



#  你的第一个 CI 实验

不用上来就搞复杂业务，我们从 **最简 FastAPI Demo** 玩起。

---

## Step 1：准备代码

```python
# main.py
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hello CI"}
```

---

## Step 2：Dockerfile

```Dockerfile
FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn
CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
```

---

## Step 3：Jenkinsfile

```groovy
pipeline {
  agent any

  stages {

    stage('Clone') {
      steps {
        git 'https://github.com/xxx/ci-demo.git'
      }
    }

    stage('Build Image') {
      steps {
        sh 'docker build -t demo:1.0 .'
      }
    }

    stage('Push') {
      steps {
        sh '''
          docker tag demo:1.0 harbor.local/demo:1.0
          docker push harbor.local/demo:1.0
        '''
      }
    }
  }
}
```



 到这一步，你已经：

✅ 完整跑通 **CI**
✅ 生成并推送镜像
✅ 为 CD 铺好跑道

---

---

---

##  CI 核心能力清单

在第一阶段，你要真正掌握 8 件事：

| 能力          | 是否必须 |
| ----------- | ---- |
| Git 日常操作    | ✅    |
| Jenkins安装   | ✅    |
| Pipeline 写法 | ✅    |
| 构建日志分析      | ✅    |
| Dockerfile  | ✅    |
| 镜像 tag 规范   | ✅    |
| 推送镜像仓库      | ✅    |
| 基础故障排错      | ✅    |

---

---

---

##  常见卡点（你大概率会遇到）

### 1️ Jenkins 无法执行 docker

```
Got permission denied while trying to connect to Docker daemon
```

解决：

```bash
sudo usermod -aG docker jenkins
systemctl restart jenkins
```



### 2️ Pipeline 失败但不明原因

正确姿势：

✅ Jenkins 控制台日志
✅ 构建失败 stage 高亮
✅ 重跑单 stage



### 3️ 镜像推不上仓库

排查三件事：

1. docker login 是否成功？
2. tag 地址是否带仓库前缀？
3. 仓库权限是否放行？



##  第一阶段毕业标准

只要你能做到：

✅ 本机 Git push
✅ Jenkins 自动拉代码
✅ Docker 构建成功
✅ push 镜像成功

—— 就已经正式完成 CI 入门 ✅



##  接下来怎么玩？

完成 CI 后，才是真正进入你感兴趣的领域：

```
CI ✅
   ↓
CD - K8S
   ↓
Ingress & ALB
   ↓
Prometheus
```



##  给你一个“立刻就能动手”的作业

如果你想**真正在今天迈出第一步**，我直接给你一个明确任务：



### ✅ 今日任务

1️ 安装 Docker
2️ 跑 Jenkins 容器：

```bash
docker run -d \
  -p 8080:8080 \
  -v jenkins:/var/jenkins_home \
  jenkins/jenkins:lts
```

3️ 创建第一个 Pipeline



##  你下一句只需要回：

 “带我装 Jenkins 并跑通第一个 Pipeline”

我就会陪你**从 0 到 CI 全链路跑通**，一步都不跳。
