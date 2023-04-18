from django.urls import path, include
from apis.goods import views as goods_views


app_name = 'goods'
app_version = 'v1'

urlpatterns = [
    path(f'{app_version}/index', goods_views.index, name='goods_index'),
    path(f'{app_version}/detail', goods_views.detail, name='goods_detail'),
    path(f'{app_version}/category', goods_views.category, name='goods_category'),

    
]