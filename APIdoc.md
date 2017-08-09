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
    "message":"login"
}
```

`获取用户名字`

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/`<int:id>`/ |无| GET|

**Return data(json):**
```
{
    "username":String
}
```

`修改用户名字`

|URL|Header|Method|
| :--- | :-- | :-- |
|/api/v1.0/`<int:id>`/ |无| PUT|

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
