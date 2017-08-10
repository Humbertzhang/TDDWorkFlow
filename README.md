# TDDWorkFlow
# 后端测试驱动开发流程
## 测试驱动开发
#### 什么是测试驱动开发（TDD）
测试驱动开发的基本思想就是在开发功能代码之前，先编写测试代码。也就是说在明确要开发某个功能后，首先思考如何对这个功能进行测试，并完成测试代码的编写，然后编写相关的代码满足这些测试用例。然后循环进行添加其他功能，直到完全部功能的开发。

#### 测试驱动开发的好处
+ 测试驱动开发可以使我们仔细思考需求，减少后期的修改
+ 在测试驱动开发过程中，我们会对相应的功能进行分解与设计，可以提高代码的内聚性与复用性
+ 测试驱动开发可以使我们快速找出Bug,并提高我们的修改代码的自信

####测试驱动开发过程

> 1） 明确当前要完成的功能。可以记录成一个 TODO 列表。
> 2） 快速完成针对此功能的测试用例编写。
> 3） 测试代码编译不通过。 
> 4） 编写对应的功能代码。 
> 5） 测试通过。 
> 6） 对代码进行重构，并保证测试通过。 
> 7） 循环完成所有功能的开发。

***

## 我们的开发流程


#### 1，确定API文档
首先，后端应根据需求进行数据库的设计，API功能的确定以及API文档的编写。
编写完API文档之后，应与一起开发的前端人员一起确定API文档中的各个API，反复修改直到达成约定。
#### 2，编写项目骨架
根据之前设计的数据库等，编写相应的models.py以及其他必不可少的组成部分，具体可见下面的实战。
#### 3，测试驱动开发API
根据测试开发的过程，编写测试以及API
## 实战
在这里，我们会编写一个带有用户系统的，前后端分离的简单Demo.他的功能是当你在注册登录后，使用GET方法访问相应API时，他会返回用户名字．使用PUT方法访问相应API时，可以修改名字．
你可以在[我的github仓库](https://github.com/Humbertzhang/TDDWorkFlow)中查看代码
#### 1，确定API文档
`注册`

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/signup/ |无| POST|

**POST data(json):**
```
{
    "username": string,     //用户名
    "password": string,     //用户密码
}
```
**Return data(json):**
```
{
    "created": int         //用户ID
}
```
`登录`

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/signin/ |无| POST|

**POST data(json):**
```
{
    "username": string,     //用户名
    "password": string,     //用户密码
}
```
**Return data(json):**
```
{
    "uid":Int
    "token":String
}
```

`获取用户名字`

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/`<int:id>`/ |Authorization:Basic Base64Token| GET|

**Return data(json):**
```
{
    "username":String
}
```

`修改用户名字`

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/`<int:id>`/ |Authorization:Basic Base64Token| PUT|

**PUT data(json):**
```
{
    "username":String
}
```
**Return data(json):**
```
{
    "message":"modiry"
}
```


#### 2，编写项目骨架
Demo的文件结构为：
```
.
├── APIdoc.md
├── Demo
│   ├── app
│   │   ├── api
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── models.py
│   ├── config.py
│   ├── manage.py
│   └── requirements.txt
└── README.md
```
根据仓库中的代码来完善好config.py manage.py requirements.txt model.py 以及各个`__init__.py`
如果你是克隆的仓库，可以使用`git checkout a1ff2d4` 来切换到搭建完骨架之后
#### 3，测试驱动开发API

在manage.py 所在的文件夹下，创建`test`文件夹，在`test`文件夹下创建`test.py`
根据仓库中的代码编写测试，并运行，得到预料中的False.
之后，根据在测试中所编写的测试用例完善api文件夹中的各个API,每次写完某个API之后就应运行一下测试(`python manage.py test`),判断是否符合预期．
若要修改功能，也应先修改测试用例，再修改API.
你分别可以使用 `git checkout <HEAD_ID>` 来跳到相应的版本

|History|HEAD ID|
| :--- | :-- |
|Test.py编写完成| cebecb4|
|Signup完成|f7c88dc|
|Signin完成|0740636|
|Getname API完成|a75f76e|
|ChangeName API完成|e3102c1|

测试前不要忘记初始化数据库！
```shell
python manage.py db init
python manage.py db migrate
python manage.py db upgrade
```
