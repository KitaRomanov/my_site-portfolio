from django.contrib import admin

from store.models import Basket, Product, ProductCategory, ProductPromo

# Register your models here.


admin.site.register(ProductCategory)

admin.site.register(ProductPromo)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')
    fields = ('name', 'description', ('price', 'quantity'), 'image', 'category', 'promo')
    readonly_fields = ()
    search_fields = ('name',)
    ordering = ('name',)


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
