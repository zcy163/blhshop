from rest_framework import serializers

from applications.goods.models import Goods


class GoodsSerializer(serializers.ModelSerializer):

  class Meta:
    model = Goods
    fields = '__all__'
