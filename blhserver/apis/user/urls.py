from django.urls import path
from apis.user import views as user_views
from apis.user import order_views


app_name = 'user'
app_version = 'v1'

urlpatterns = [
    path(f'{app_version}/token', user_views.token, name='token'),
    path(f'{app_version}/address/add', user_views.address_add, name='address_add'),
    path(f'{app_version}/address/list', user_views.address_list, name='address_list'),
    path(f'{app_version}/address/del', user_views.address_del, name='address_del'),
    path(f'{app_version}/address/detail', user_views.address_detail, name='address_detail'),
    # order
    path(f'{app_version}/order/list', order_views.order_list, name='order_list'),
    path(f'{app_version}/order/add', order_views.order_add, name='order_add'),
]
