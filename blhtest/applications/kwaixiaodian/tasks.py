from celery import shared_task, Task

from applications.kwaixiaodian.sign import KwaixiaodianSign


kwaixiaodianSign = KwaixiaodianSign()

@shared_task(base=Task, bind=True)
def refresh_token(self):
  """定时刷新快手平台access_token"""
  res = kwaixiaodianSign.refresh_token()
  return self.name, res

