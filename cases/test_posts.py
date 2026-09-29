# ============================================
# test_posts.py —— 用例层（只写测试逻辑）
# 不再直接 import requests，而是调 api 层的函数
# 这样用例读起来就是"测什么"，非常清晰
# ============================================

import pytest
from api.posts_api import get_post, get_posts, create_post, delete_post


def test_get_single_post():
    """获取单条帖子：应 200 且 id 正确"""
    resp = get_post(1)
    assert resp.status_code == 200
    assert resp.json()["id"] == 1


def test_get_post_list():
    """获取帖子列表：应 200 且有数据"""
    resp = get_posts()
    assert resp.status_code == 200
    assert len(resp.json()) > 0


def test_create_post():
    """新增帖子：应 201"""
    resp = create_post("测试标题", "测试内容")
    assert resp.status_code == 201


@pytest.mark.parametrize("post_id, expected", [
    (1, 200),        # 正常
    (100, 200),      # 边界：最后一个存在的 id
    (101, 404),      # 边界外
    (0, 404),        # 边界
    (99999, 404),    # 异常
    (-1, 404),       # 负数边界
    (1000000, 404),  # 超大数
])
def test_get_post_status(post_id, expected):
    """不同 id 的状态码：参数化测多组"""
    resp = get_post(post_id)
    assert resp.status_code == expected
