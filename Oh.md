#Oh.ProTest

##流程

####1.构建镜像
```shell
docker build -t 镜像名 .路径
例:
docker build -t spring263 .
```
####2.运行容器
```shell
docker run -it -d --cpus 核心数 -m 内存上限 -p 物理机端口:容器端口 --name 容器名 镜像名:tag
例:
docker run -it -d --cpus 1 -m 500m -p 8000:8080 --name test1 spring263:1
```