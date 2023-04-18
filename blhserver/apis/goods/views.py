from django.http import HttpResponse
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view, permission_classes, parser_classes
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.parsers import MultiPartParser, JSONParser, FileUploadParser
from rest_framework.authtoken.models import Token
from django.db.models import IntegerField

from applications.goods.models import Goods,Category
from apis.goods.serializers import GoodsSerializer
from response_v1.response import APIResponse
from blhserver.utils.pagination import pageNumberPagination
from django.db.models.functions import Cast
from applications.kwaixiaodian.kwaixiaodian import Kwaixiaodian

import logging


logger = logging.Logger('console')
kwaixiaodian = Kwaixiaodian()

@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def index(request):
  """不限制接口权限"""
  
  
  sort = request.data['sort']
  sequence = request.data['sequence']
  filters = request.data['filters']
  search = request.data.get('search', '')

  goods_filter = Goods.objects.filter(item_category_name__contains=filters, item_title__contains=search)

  if sort:
    goods = goods_filter.annotate(item=Cast(sort, IntegerField())).order_by(sequence + 'item')
    # goods = Goods.objects.all().annotate(item=Cast(sort, IntegerField())).order_by(sequence + 'item')
  else:
    goods = goods_filter
  
  
  page = pageNumberPagination()
  data = page.data(request, goods, GoodsSerializer)
  
  return APIResponse(data)


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def detail(request):
  """不限制接口权限"""
  
  itemId = request.data['itemId']
  
  goods = kwaixiaodian.query_selection_item_detail({'itemId': [itemId]})
  
  if not goods.get('result') == 1:
    return APIResponse(code=goods.get('result'), msg=goods.get('msg'))
  
  return APIResponse(goods.get('itemList')[0] or {})


@api_view(['POST'])
@permission_classes((AllowAny,))
@parser_classes([JSONParser])
def category(request):
  """不限制接口权限"""
  
  category_list =  Category.objects.values('category_name').distinct()
  if not category_list:
    return APIResponse(code=-1,msg='category_list get failed!')
    
  return APIResponse(category_list or {})
