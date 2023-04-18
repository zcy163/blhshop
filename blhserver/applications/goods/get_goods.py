
from applications.kwaixiaodian.kwaixiaodian import Kwaixiaodian
from applications.goods.models import Goods, Category

from django.db.utils import IntegrityError

import threading
import time


kwaixiaodian = Kwaixiaodian()
activity_retry_count = 3
goods_retry_count = 3

def query_activity_id_list():
    """
    团长查询招商活动列表
    """

    global activity_retry_count

    # 获取平台接口结果
    param = {"offset": 0, "limit": 1}
    result = kwaixiaodian.investment_activity_open_list(param)
    
    try:
        total = result.get('data').get('total')
        
        param = {"offset": 0, "limit": total}
        result = kwaixiaodian.investment_activity_open_list(param)
        
        activitys = [activity.get('activityId') for activity in result.get('data').get('result')]
        
        return activitys
    except AttributeError:
        if not activity_retry_count == 0:
            query_activity_id_list()
            activity_retry_count -= 1
        
    return []

def query_goods_list(activity_id):

    global goods_retry_count
    
    param = {"activityId": activity_id, "limit": 1}
    result = kwaixiaodian.investment_activity_open_item_list(param)
    
    try:
        total = result.get('data').get('total')
        param = {"activityId": activity_id, "limit": total}
        result = kwaixiaodian.investment_activity_open_item_list(param)

        goods_list = result.get('data').get('activityItemDataList')
        # 
        [save_goods_db(activity_id, goods) for goods in goods_list if goods.get('itemAuditStatus') == 2]
        
        return goods_list
    except AttributeError:
        if not goods_retry_count == 0:
            query_goods_list(activity_id)
            goods_retry_count -= 1
        
    return []

def save_goods_db(activity_id, goods):
    # print(activity_id, goods)
    # with open("./log.txt", "a+") as f:
    #     f.write(f"{activity_id}{goods}")
    
    category_name = goods.get('itemCategoryName')
    if category_name:
        save_category_db(category_name)
    
    goods['activityId'] = activity_id
    db_goods = {}
    
    for field in Goods._meta.fields:
        if str2Hump(field.name) in goods:
            db_goods[field.name] = goods[str2Hump(field.name)]
    
    # print(db_goods)
    try:
        Goods.objects.create(**db_goods)
    except IntegrityError:
        goods = Goods.objects.get(item_id=goods['itemId'])
        goods_activity_id = goods.activity_id
        goods.activity_id = f"{goods_activity_id},{activity_id}"
        goods.save()
    
    return goods

def save_category_db(category_name):
    
    category = category_name.split(">")[0]
    if not category:
        return

    categorys = category.split('/')
    if not category:
        return
    
    for category in categorys:
        if category:
            category_db = Category.objects.filter(category_name=category)
            if not category_db:
                Category.objects.create(category_name=category)
    

def get_lower_case_name(text):
    lst = []
    for index, char in enumerate(text):
        if char.isupper() and index != 0:
            lst.append("_")
        lst.append(char)

    return "".join(lst).lower()

def str2Hump(text):
    arr = filter(None, text.lower().split('_'))
    res = ''
    j = 0
    for i in arr:
        if j == 0:
            res = i
        else:
            res = res + i[0].upper() + i[1:]
        j += 1
    return res

def clear_goods_db():
    Goods.objects.all().delete()
    
def clear_category_db():
    Category.objects.all().delete()


def save_goods_db_main():
    
    activity_threads = []
    activity_step = 0
    activity_length = 50
    activity_ids = query_activity_id_list()
    
    # t = threading.Thread(target=query_goods_list, args=(activity_ids[0],))
    # t.start()
    
    clear_goods_db()
    clear_category_db()
    
    for activity_id in activity_ids:
        t = threading.Thread(target=query_goods_list, args=(activity_id,))
        activity_threads.append(t)
        
    while len(activity_threads) > activity_step * activity_length:
        current = activity_step * activity_length
        for t in activity_threads[current:current+activity_length]:
            t.start()
        activity_step += 1
        time.sleep(1)
        
    
    
    
    
    