from django.urls import path
from apis.wxamp import views as wxamp_views


app_name = 'wxamp'
app_version = 'v1'

urlpatterns = [
    path(f'{app_version}/jscode2session', wxamp_views.jscode2session, name='jscode2session'),
]
