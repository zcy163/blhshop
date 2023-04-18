from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.conf import settings

from applications.kwaixiaodian.sign import KwaixiaodianSign
from applications.kwaixiaodian.datas import datas as kwaixiaodian_datas

from urllib.parse import urlencode
import os
import requests
import qrcode


kwaixiaodianSign = KwaixiaodianSign()

def authorize(request):
    """
    获取授权码code
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/oauth2/authorize
    """
    data = kwaixiaodian_datas.get("AUTHORIZE_DATA")
    return HttpResponseRedirect(f"{settings.KUAISHOU_HOST}/oauth2/authorize?{urlencode(data)}")

def authorize_qrcode(request):
    """
    获取授权码code
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/oauth2/authorize_qrcode
    """
    data = kwaixiaodian_datas.get("AUTHORIZE_DATA")
    authorize_url = f"{settings.KUAISHOU_HOST}/oauth2/authorize?{urlencode(data)}"
    qrcode_img_path = os.path.join(settings.BASE_DIR, "applications/kwaixiaodian/qrcode/authorize.png")
    qrcode_img = qrcode.make(authorize_url).save(qrcode_img_path)
    with open(qrcode_img_path, 'rb') as f:
        qrcode_img_data = f.read()
    return HttpResponse(qrcode_img_data, content_type="image/png")

def access_token(request):
    """
    用授权码code换取长时令牌refreshToken以及访问令牌accessToken
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/oauth2/access_token
    """
    code = request.GET.get("code", "")
    return JsonResponse(kwaixiaodianSign.access_token(code))

def refresh_token(request):
    """
    用长时令牌refreshToken刷新访问令牌accessToken
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/oauth2/refresh_token
    """
    return JsonResponse(kwaixiaodianSign.refresh_token())

def sign(request):
    """
    签名计算
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/oauth2/sign
    """
    method = request.GET.get("method", "open.distribution.investment.my.create.activity.list")
    param = request.GET.get("param", {})
    return JsonResponse(kwaixiaodianSign.get_sign(method, param))
