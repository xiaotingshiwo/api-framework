# 接口自动化测试框架（pytest + requests）

对 jsonplaceholder 免费测试接口做自动化测试的练习项目。

## 项目结构（分层设计）

```
api-framework/
├── config.py            # 配置层：统一管理 BASE_URL
├── conftest.py          # pytest 钩子文件（让 import 生效）
├── common/
│   └── request_util.py  # 公共层：封装请求、打印日志
├── api/
│   └── posts_api.py     # 接口层：把每个接口封装成函数
├── cases/
│   └── test_posts.py    # 用例层：只写测试逻辑
└── README.md
```

## 为什么分层

把「配置 / 请求 / 接口 / 用例」分开的好处：

1. 改接口地址 → 只改 `config.py`
2. 换请求库 / 加鉴权 → 只改 `common/request_util.py`
3. 用例层只关注"测什么"，不关心"怎么发请求"

## 技术点

- requests：发 HTTP 请求
- pytest：测试框架 + `@pytest.mark.parametrize` 参数化
- 分层架构：config / common / api / cases

## 运行方式

进入本目录后执行：

```
python -m pytest cases/test_posts.py -v
```
