from django.db import models

from blhserver.utils.models import BaseModel

# Create your models here.


class Goods(BaseModel):
  """团长招商活动已报名商品列表"""
  
  WEB_URL_TYPE = (
      ('1','小店'),
      ('2','快分销')
  )
  activity_id = models.CharField(max_length=255, verbose_name=u'活动ID')

  item_title = models.CharField(max_length=255, verbose_name=u'商品标题')
  
  item_id = models.CharField(max_length=255, verbose_name=u'商品id', primary_key=True)
  
  item_img_url = models.CharField(max_length=255, verbose_name=u'商品图片链接')
  
  item_stock = models.CharField(max_length=255, verbose_name=u'商品库存')
  
  item_price = models.CharField(max_length=255, verbose_name=u'商品价格')
    
  item_category_name = models.CharField(max_length=255, verbose_name=u'商品类目名称')
  
  item_volume = models.CharField(max_length=255, verbose_name=u'商品销量')
  
  web_url_type = models.CharField(choices=WEB_URL_TYPE,max_length=1,default='',verbose_name=u'1=小店；2=快分销')

  item_commission_rate = models.CharField(max_length=255, verbose_name=u'商品佣金率')
  
  item_apply_time = models.CharField(max_length=255, verbose_name=u'商品报名时间')  
  
  investment_promotion_rate = models.CharField(max_length=255, verbose_name=u'团长服务费率')

  
  def save(self, *args, **kwargs):
    """
    重写父类的save方法，自定实现uid的成功和存储
    """
    super(Goods, self).save(*args, **kwargs)
    
    

# 说明
  class Meta:
    db_table = "Goods"  # 如果不设置，就会是用django默认的数据表命名方式
    verbose_name = "团长招商活动已报名商品列表"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.item_id
    
    

class Category(BaseModel):
  category_name = models.CharField(max_length=255, verbose_name=u'商品类目名称')
  
  
  
  def save(self, *args, **kwargs):
    """
    重写父类的save方法，自定实现uid的成功和存储
    """
    super(Category, self).save(*args, **kwargs)
    
    

# 说明
  class Meta:
    db_table = "Category"  # 如果不设置，就会是用django默认的数据表命名方式
    verbose_name = "团长招商活类目列表"
    verbose_name_plural = verbose_name

  def __str__(self):
    return self.category_name