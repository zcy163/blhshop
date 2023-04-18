from applications.kwaixiaodian.utils import create_requests_get


class Kwaixiaodian:


    def public_category_list(self, data={}):
        """
        类目信息列表
        """

        method = "open.distribution.public.category.list"
        param = {}
        # 添加请求参数
        param.update(data or {})
        # 获取平台接口结果
        return create_requests_get(method, param).json()

    def investment_activity_open_list(self, data={}):
        """
        团长查询招商活动列表
        """

        # 默认配置和参数
        method = "open.distribution.investment.activity.open.list"
        param = {"offset": 0, "limit": 100}
        # 添加请求参数
        param.update(data or {})
        # 获取平台接口结果
        return create_requests_get(method, param).json()


    def investment_activity_open_item_list(self, data={}):
        """
        团长招商活动已报名商品列表
        """
        
        # 默认配置和参数
        method = "open.distribution.investment.activity.open.item.list"
        param = {"activityId": "1734669243", "limit": 100}
        # 添加请求参数
        param.update(data or {})
        # 获取平台接口结果
        return create_requests_get(method, param).json()

    def query_selection_item_detail(self, data={}):
        """
        团长招商活动已报名商品列表
        """
        
        # 默认配置和参数
        method = "open.distribution.query.selection.item.detail"
        param = {"itemId": []}
        # 添加请求参数
        param.update(data or {})
        # 获取平台接口结果
        return create_requests_get(method, param).json()

