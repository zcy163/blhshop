"""blhserver URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    # 快手电商平台接口
    path('rest/1.0/kwaixiaodian/', include('applications.kwaixiaodian.urls', namespace='kwaixiaodian')),
    # goods_views
    path('rest/goods/', include('apis.goods.urls', namespace='goods')),
    # 微信平台
    path('rest/1.0/wxamp/', include('apis.wxamp.urls', namespace='wxamp')),
    # user
    path('rest/1.0/user/', include('apis.user.urls', namespace='user')),
]
