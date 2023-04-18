from django_redis import get_redis_connection
from django.conf import settings

from applications.kwaixiaodian.datas import datas as kwaixiaodian_datas

from urllib.parse import urlencode, quote
from datetime import datetime
import json
import hashlib
import requests


class KwaixiaodianSign:
    """KwaixiaodianSign"""

    # 链接redis
    redis_conn = get_redis_connection('default')
    # 过期时间，48小时
    expires = 60 * 60 * 48

    def __requests_res(self, res):
        """通用处理返回结果"""
        if res.status_code == 200 and res.json().get('result') == 1:
            self.set_token(res.json())
        return res.json()

    def set_access_token(self, access_token):
        """保存access_token"""
        self.redis_conn.set('access_token', access_token, self.expires)

    def get_access_token(self):
        """获取access_token"""
        return self.redis_conn.get('access_token')

    def set_refresh_token(self, refresh_token):
        """保存refresh_token"""
        self.redis_conn.set('refresh_token', refresh_token, self.expires)

    def get_refresh_token(self):
        """获取access_token"""
        return self.redis_conn.get('refresh_token')

    def set_token(self, data):
        """将token添加到redis，接收json对象，包含access_token和refresh_token字段"""
        self.set_access_token(data.get("access_token", ""))
        self.set_refresh_token(data.get("refresh_token", ""))

    def get_sign(self, method, param):
        """签名计算"""
        sign_data = kwaixiaodian_datas.get("SIGN_DATA")
        data = {}
        data.update(sign_data or {})
        data["method"] = method
        data["param"] = json.dumps(param).replace(" ", "")
        data["access_token"] = self.get_access_token()
        data["timestamp"] = int(datetime.timestamp(datetime.now()) * 1000)
        # 将data转成url参数
        format_data = "&".join("{}={}".format(*i) for i in data.items())
        # md5加密
        m = hashlib.md5()
        m.update(format_data.encode())
        sign = m.hexdigest()
        # 签名保存到redis
        self.redis_conn.set('sign', sign, self.expires)
        # 生成系统参数
        # data["param"] = quote(json.dumps(param).replace(" ", ""))
        data["sign"] = sign
        # 添加额外请求参数
        data.update(param or {})
        # 第一个参数是签名，第二个参数是请求接口时需要使用的完整系统参数
        return data

    def access_token(self, code):
        """从快手平台获取access_token"""
        params = kwaixiaodian_datas.get("ACCESS_TOKEN_PARAMS")
        params["code"] = code
        res = requests.get(f"{settings.KWAIXIAODIAN_HOST}/oauth2/access_token", params=params)
        return self.__requests_res(res)

    def refresh_token(self):
        """刷新access_token"""
        data = kwaixiaodian_datas.get("REFRESH_TOKEN_DATA")
        data["refresh_token"] = self.get_refresh_token()
        res = requests.post(f"{settings.KWAIXIAODIAN_HOST}/oauth2/refresh_token", data=data)
        return self.__requests_res(res)




