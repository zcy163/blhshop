from django.http import JsonResponse

from applications.kwaixiaodian.utils import create_requests_get
from applications.kwaixiaodian.kwaixiaodian import Kwaixiaodian


kwaixiaodian = Kwaixiaodian()

def api_test(request):
    """
    黑名单测试
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/test
    """
    return JsonResponse({})

def api_public_category_list(request):
    """
    类目信息列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/public/category/list
    """
    # 获取平台接口结果
    result = kwaixiaodian.public_category_list(request.GET.dict())
    return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

def api_investment_activity_open_list(request):
    """
    团长查询招商活动列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/investment/activity/open/list
    """
    # 获取平台接口结果
    result = kwaixiaodian.investment_activity_open_list(request.GET.dict())
    return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

def api_investment_activity_open_item_list(request):
    """
    团长招商活动已报名商品列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/investment/activity/open/item/list
    """
    # 获取平台接口结果
    result = kwaixiaodian.investment_activity_open_item_list(request.GET.dict())
    return JsonResponse(result, json_dumps_params={"ensure_ascii": False})

def api_query_selection_item_detail(request):
    """
    团长招商活动已报名商品列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/query/selection/item/detail
    """
    # 获取平台接口结果
    result = kwaixiaodian.query_selection_item_detail(request.GET.dict())
    return JsonResponse(result, json_dumps_params={"ensure_ascii": False})




