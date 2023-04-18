from rest_framework.response import Response

class APIResponse(Response):
    def __init__(self, data={}, code=0, msg=''):
      # 自定制返回结果
      idy_data = { 'code': code, 'data': data, 'msg': msg }
      super().__init__(idy_data)