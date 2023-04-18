from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from django.conf import settings

from apis.user.serializers import UserSerializer
from applications.user.models import User
from response_v1.response import APIResponse

import requests


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def jscode2session(request):

    params = {
        'appid': settings.WXAMP_APPID,
        'secret': settings.WXAMP_SECRET,
        'js_code': request.data.get('js_code', ''),
        'grant_type': settings.WXAMP_GRANT_TYPE
    }

    res = requests.get(settings.WXAMP_JSON2SEESSION_URL, params=params).json()
    if res.get('errcode'):
        return APIResponse(code=res.get('errcode'), msg=res.get('errmsg'))

    session_key = res.get('session_key', '')
    openid = res.get('openid', '')

    try:

        user = User.objects.get(openid=openid)
        user.session_key = session_key
        user.save()
        token, _ = Token.objects.get_or_create(user=user)

    except User.DoesNotExist:

        data = {
            'username': request.data.get('username', ''),
            'password': '123456',
            'image': request.data.get('image', ''),
            'openid': openid,
            'session_key': session_key
        }

        serializer = UserSerializer(data=data)
        if not serializer.is_valid():
            return APIResponse(code=1, msg=serializer.errors)

        instance = serializer.save()
        token, _ = Token.objects.get_or_create(user=instance)
        if not token:
            return APIResponse(code=1, msg='创建授权时异常。')

    return APIResponse({'token': token.key})
