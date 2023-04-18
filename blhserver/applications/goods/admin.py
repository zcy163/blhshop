from django.contrib import admin
from applications.goods.models import Goods, Category

# Register your models here.

@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    list_display = ('item_id', 'activity_id', 'item_title', 'create_time')
    
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'create_time')
