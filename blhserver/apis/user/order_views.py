from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.conf import settings

from apis.user.serializers import UserSerializer, AddressSerializer, OrderSerializer
from applications.user.models import Order, Address
from applications.goods.models import Goods
from response_v1.response import APIResponse
from blhserver.utils.pagination import pageNumberPagination

import requests


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def order_list(request):
    
    token = request.data.get('token')

    try:
        token_instance = Token.objects.get(key=token)
        user_instace = token_instance.user
        orders_instance = user_instace.orders.all().order_by('-create_time')
    except Token.DoesNotExist:
        if token:
            return APIResponse(code=1, msg="token is doesn't")
        else:
            orders_instance = Order.objects.all().order_by('-create_time')

    page = pageNumberPagination()
    data = page.data(request, orders_instance, OrderSerializer)

    return APIResponse(data)


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def order_add(request):

    token = request.data.get('token')
    goods = request.data.get('goods')
    address = request.data.get('address')

    # print(token, goods, address)

    try:
        token_instance = Token.objects.get(key=token)
        user_instace = token_instance.user
    except Token.DoesNotExist:
        return APIResponse(code=1, msg="token is doesn't")

    try:
        goods_instance = Goods.objects.get(item_id=goods)
    except Goods.DoesNotExist:
        return APIResponse(code=1, msg="goods is doesn't")

    try:
        address_instance = Address.objects.get(id=address)
    except Address.DoesNotExist:
        return APIResponse(code=1, msg="address is doesn't")

    data = {
        'user': user_instace.id,
        'goods': goods_instance.item_id,
        'address': address_instance.id
    }

    order_serializer = OrderSerializer(data=data)

    if not order_serializer.is_valid():
        return APIResponse(code=1, msg=order_serializer.errors)

    order_serializer.save() 

    return APIResponse()


