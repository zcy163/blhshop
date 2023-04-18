from django.urls import path, include
from applications.kwaixiaodian import views as kwaixiaodian_views
from applications.kwaixiaodian import apis as kwaixiaodian_apis

import importlib


app_name = 'kwaixiaodian'
app_version = 'v1'

urlpatterns = []
# 鉴权路由
urlpatterns.extend([
    path(f'{app_version}/oauth2/authorize', kwaixiaodian_views.authorize, name='authorize'),
    path(f'{app_version}/oauth2/authorize_qrcode', kwaixiaodian_views.authorize_qrcode, name='authorize_qrcode'),
    path(f'{app_version}/oauth2/access_token', kwaixiaodian_views.access_token, name='access_token'),
    path(f'{app_version}/oauth2/refresh_token', kwaixiaodian_views.refresh_token, name='refresh_token'),
    path(f'{app_version}/oauth2/sign', kwaixiaodian_views.sign, name='sign'),
])

# 接口路由，动态加载黑名单以外的所有api_开头函数
blacklist = ["api_test"]
for api_def in dir(kwaixiaodian_apis):
    # 加载以api_开通并且不在黑名单中的接口
    if api_def.startswith("api_") and not api_def in blacklist:
        api_name = api_def.lstrip("api").lstrip("_")
        mkwaixiaodian_odule = importlib.import_module("applications.kwaixiaodian.apis")
        pathurl = f'{app_version}/{api_name.replace("_", "/")}'
        urlpatterns.append(path(pathurl, getattr(mkwaixiaodian_odule, api_def), name=api_name))
