from django.contrib.auth import get_user_model
from rest_framework import serializers

from applications.user.models import Address, Order
from applications.goods.models import Goods
from apis.goods.serializers import GoodsSerializer


User = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    name = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    id_card_number = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    address = serializers.SerializerMethodField()
    orders = serializers.SerializerMethodField()

    def get_address(self, instance):

        # return instance.addresses.all()
        return []

    def get_orders(self, instance):

        # return instance.orders.all()
        return []

    class Meta:
        model = User
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):

    mobile = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    place = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    receiver = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    title = serializers.CharField(required=False, allow_null=True, allow_blank=True)

    class Meta:

        model = Address
        fields = '__all__'


class OrderSerializer(serializers.ModelSerializer):

    status = serializers.CharField(required=False, allow_null=True, allow_blank=True)
    goodsInfo = serializers.SerializerMethodField()

    def get_goodsInfo(self, instance):

        goods_id = instance.goods

        try:
            goods_instance = Goods.objects.get(item_id=goods_id)
            goods_serializer = GoodsSerializer(instance=goods_instance)
            return [goods_serializer.data]
        except Goods.DoesNotExist:
            return []

    class Meta:

        model = Order
        fields = ['id', 'goods', 'address', 'uid', 'status', 'update_time', 'user', 'create_time', 'goodsInfo']

