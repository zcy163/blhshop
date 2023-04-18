from django.http import JsonResponse

from applications.kwaixiaodian.utils import create_requests_get, create_requests_post


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

    method = "open.distribution.public.category.list"
    param = {}

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_cps_promotion_reco_topic_list(request):
    """
    获取推荐专题列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/cps/promotion/reco/topic/list
    """

    method = "open.distribution.cps.promotion.reco.topic.list"
    param = {}

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_cps_promotion_theme_entrance_list(request):
    """
    获取站外分销专题列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/cps/promotion/theme/entrance/list
    """

    method = "open.distribution.cps.promotion.theme.entrance.list"
    param = {}

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_investment_my_create_activity_list(request):
    """
    查询我发起的招商活动
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/investment/my/create/activity/list
    """

    method = "open.distribution.investment.my.create.activity.list"
    param = {
        "offset": 0
    }
    # param = {}

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_cps_kwaimoney_selection_channel_list(request):
    """
    获取站外分销选品频道列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/cps/kwaimoney/selection/channel/list
    """

    method = "open.distribution.cps.kwaimoney.selection.channel.list"
    param = {}

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_cps_kwaimoney_selection_item_list(request):
    """
    获取站外分销商品列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/cps/kwaimoney/selection/item/list
    """

    method = "open.distribution.cps.kwaimoney.selection.item.list"
    param = {
        "pageSize": 20,
        # "channelId": [99,3,111],
        "planType": 1,
    }

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_cps_promotion_reco_topic_item_list(request):
    """
    获取推荐专题商品列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/cps/promotion/reco/topic/item/list
    """

    method = "open.distribution.cps.promotion.reco.topic.item.list"
    param = {
        "topicId": 8,
    }

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})

def api_investment_activity_open_list(request):
    """
    团长查询招商活动列表
    https://wxamp.blhlm.com/rest/1.0/kwaixiaodian/v1/investment/activity/open/list
    """
    
    method = "open.distribution.investment.activity.open.list"
    param = {
        "limit": 1,
    }

    res = create_requests_get(method, param)
    return JsonResponse(res.json(), json_dumps_params={"ensure_ascii":False})





