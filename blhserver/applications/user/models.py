from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core import validators

from blhserver.utils.models import BaseModel
from applications.goods.models import Goods

import uuid


# 继承AbstractUser类
class User(AbstractUser, BaseModel):
    """
    自定义User表
    """
    name = models.CharField(
        verbose_name="姓名",
        help_text="身份证上的真实姓名",
        max_length=30,
        default="")

    id_card_number = models.CharField(
        verbose_name="身份证件号",
        help_text="身份证件号",
        max_length=18,
        default="")

    mobile = models.CharField(
        verbose_name="手机号码",
        help_text="手机号码：用于接收验证码",
        max_length=11,
        default="",
        unique=True,
        validators=[validators.RegexValidator(regex=r"^1[3-8]\d{9}$", message="请输入正确格式的手机号码！")],
        error_messages={"unique": "您输入的手机号码已经存在！", "required": "手机号码不能为空！"})

    default_address = models.ForeignKey(
        'Address',
        related_name='users',
        null=True,
        blank=True,
        on_delete=models.SET_NULL, verbose_name='默认地址')

    uid = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        default="",
        verbose_name='uid')

    # image = models.ImageField(verbose_name='用户头像', null=True, upload_to=user_upload_location)

    image = models.CharField(max_length=255, default="")
    session_key = models.CharField(max_length=255, default="")
    openid = models.CharField(max_length=255, default="")

    REQUIRED_FIELDS = ['mobile']

    def save(self, *args, **kwargs):
        """
        重写父类的save方法，自定实现uid的成功和存储
        """
        if not self.uid or self.uid == '':
            self.uid = uuid.uuid4().hex
        super(User, self).save(*args, **kwargs)

    # 这个类，是对User类的一个说明
    class Meta:
        db_table = "user"  # 如果不设置，就会是用django默认的数据表命名方式
        verbose_name = "用户表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class Address(BaseModel):
    """用户地址"""
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='addresses', verbose_name='用户')
    title = models.CharField(max_length=20, verbose_name='地址名称')
    receiver = models.CharField(max_length=20, verbose_name='收货人')
    place = models.CharField(max_length=50, verbose_name='地址')
    mobile = models.CharField(max_length=11, verbose_name='手机')
    tel = models.CharField(max_length=20, null=True, blank=True, default='', verbose_name='固定电话')
    email = models.CharField(max_length=30, null=True, blank=True, default='', verbose_name='电子邮箱')
    is_deleted = models.BooleanField(default=False, verbose_name='逻辑删除')

    addressTag = models.CharField(max_length=255, null=True, blank=True, default='')
    cityCode = models.CharField(max_length=255, null=True, blank=True, default='')
    cityName = models.CharField(max_length=255, null=True, blank=True, default='')
    detailAddress = models.CharField(max_length=255, null=True, blank=True, default='')
    districtCode = models.CharField(max_length=255, null=True, blank=True, default='')
    districtName = models.CharField(max_length=255, null=True, blank=True, default='')
    isDefault = models.CharField(max_length=255, null=True, blank=True, default='')
    name = models.CharField(max_length=255, null=True, blank=True, default='')
    phone = models.CharField(max_length=255, null=True, blank=True, default='')
    provinceCode = models.CharField(max_length=255, null=True, blank=True, default='')
    provinceName = models.CharField(max_length=255, null=True, blank=True, default='')

    class Meta:
        db_table = 'address'
        verbose_name = '用户地址'
        verbose_name_plural = verbose_name
        ordering = ['-update_time']

    def __str__(self):
        return f"{self.cityName}-{self.provinceName}-{self.districtName}-{self.detailAddress}"

class Order(BaseModel):

    status_choices = (
        (0, '已完成'),
        (1, '待审批'),
        (2, '撤销')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders', verbose_name='用户')
    address = models.ForeignKey(Address, on_delete=models.CASCADE, related_name='orders', verbose_name='地址')
    goods = models.ForeignKey(
        Goods,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='商品',
        to_field='item_id')

    status = models.IntegerField(choices=status_choices, default=1)

    uid = models.CharField(
        max_length=32,
        unique=True,
        null=True,
        blank=True,
        default="",
        verbose_name='uid')

    def save(self, *args, **kwargs):
        """
        重写父类的save方法，自定实现uid的成功和存储
        """
        if not self.uid or self.uid == '':
            self.uid = uuid.uuid4().hex
        super(Order, self).save(*args, **kwargs)

    # 这个类，是对User类的一个说明
    class Meta:
        db_table = "order"  # 如果不设置，就会是用django默认的数据表命名方式
        verbose_name = "订单表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.uid
