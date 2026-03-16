"""
Tavily 注册核心模块
当前站点真实注册流已切换为浏览器 + 邮箱 6 位验证码。
"""
from mail_provider import create_email, get_verification_link


def register(email, password):
    """统一走已实测通过的浏览器注册链路"""
    from tavily_browser_solver import register_with_browser_solver

    return register_with_browser_solver(email, password)
