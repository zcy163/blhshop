from celery import shared_task, Task

from applications.goods.get_goods import save_goods_db_main

@shared_task(base=Task, bind=True)
def save_goods(self):
  """"""
  save_goods_db_main()
  return self.name

