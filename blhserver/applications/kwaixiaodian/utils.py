from django.conf import settings

from applications.kwaixiaodian.sign import KwaixiaodianSign

import requests


kwaixiaodianSign = KwaixiaodianSign()

def create_url(method, host=""):
    """
    根据method拼接完整接口rul
    """
    path = method.replace(".", "/")
    return f"{host or settings.KWAIXIAODIAN_API_HOST}/{path}"


def create_requests_get(method, param):
    """GET请求"""

    # 获取接口url
    url = create_url(method)
    # 获取系统参数
    data = kwaixiaodianSign.get_sign(method, param)
    # 请求接口
    return requests.get(url, params=data)

def create_requests_post(method, param):
    """POST请求"""

    # 获取接口url
    url = create_url(method)
    # 获取系统参数
    data = kwaixiaodianSign.get_sign(method, param)
    # 请求接口
    return requests.get(url, data=data)
