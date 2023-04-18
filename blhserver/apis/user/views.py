from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.conf import settings

from apis.user.serializers import UserSerializer, AddressSerializer
from applications.user.models import User, Address
from response_v1.response import APIResponse

import requests


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def token(request):

    token = request.data.get('token', '')
    # print(token)

    try:
        token_instance = Token.objects.get(key=token)
    except Token.DoesNotExist:
        return APIResponse(code=1, msg="token is doesn't")

    serializer = UserSerializer(instance=token_instance.user)

    return APIResponse(serializer.data)


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def address_add(request):

    id = request.data.get('id', 0)
    token = request.data.get('token', '')
    # print(token)

    try:
        token_instance = Token.objects.get(key=token)
        request.data['user'] = token_instance.user.id
    except Token.DoesNotExist:
        return APIResponse(code=1, msg="token is doesn't")

    try:
        address = Address.objects.get(id=id)
        serializer = AddressSerializer(instance=address, data=request.data)
    except Address.DoesNotExist:
        serializer = AddressSerializer(data=request.data)
    
    if not serializer.is_valid():
        return APIResponse(code=1, msg=serializer.errors)

    serializer.save()

    return APIResponse({})


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def address_list(request):

    token = request.data.get('token', '')
    # print(token)

    try:
        token_instance = Token.objects.get(key=token)
    except Token.DoesNotExist:
        return APIResponse(code=1, msg="token is doesn't")

    addresses = token_instance.user.addresses.all()

    serializer = AddressSerializer(addresses, many=True)

    return APIResponse(serializer.data)

@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def address_del(request):

    try:
        address = Address.objects.get(id=request.data.get('id', 0))
        address.delete()
    except Address.DoesNotExist:
        return APIResponse(code=1, msg="address is doesn't")

    return APIResponse({})


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def address_detail(request):

    try:
        address = Address.objects.get(id=request.data.get('id', 0))
        serializer = AddressSerializer(instance=address)
    except Address.DoesNotExist:
        return APIResponse(code=1, msg="address is doesn't")

    return APIResponse(serializer.data) 

