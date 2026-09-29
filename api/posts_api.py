# ============================================
# posts_api.py —— 接口封装层
# 把"帖子"相关的接口，封装成一个个函数
# 用例层只调这里，不直接碰 requests
# ============================================

from common.request_util import get, post, delete


def get_post(post_id):
    """获取单条帖子"""
    return get(f"/posts/{post_id}")


def get_posts():
    """获取帖子列表"""
    return get("/posts")


def create_post(title, body, user_id=1):
    """新增帖子"""
    return post("/posts", {"title": title, "body": body, "userId": user_id})


def delete_post(post_id):
    """删除帖子"""
    return delete(f"/posts/{post_id}")
