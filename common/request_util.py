# ============================================
# request_util.py —— 请求封装层（公共能力）
# 把 requests 再包一层：统一拼接 URL、统一打印日志
# 好处：以后要加鉴权、改请求方式，只改这一个文件
# ============================================

import requests
from config import BASE_URL


# 创建一个 Session，并关闭"读取系统代理"功能（trust_env = False）
# 这样测试就不会被本机代理/VPN 的状态影响（否则代理一关，所有请求都会失败）
session = requests.Session()
session.trust_env = False


def get(path, params=None):
    """发 GET 请求，返回响应对象"""
    url = BASE_URL + path
    resp = session.get(url, params=params)
    print(f"[GET] {url} -> 状态码 {resp.status_code}")
    return resp


def post(path, json_body=None):
    """发 POST 请求，返回响应对象"""
    url = BASE_URL + path
    resp = session.post(url, json=json_body)
    print(f"[POST] {url} -> 状态码 {resp.status_code}")
    return resp


def delete(path):
    """发 DELETE 请求，返回响应对象"""
    url = BASE_URL + path
    resp = session.delete(url)
    print(f"[DELETE] {url} -> 状态码 {resp.status_code}")
    return resp
