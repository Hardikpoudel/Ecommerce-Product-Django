from .models import products, category, subCat, dailyDeals, seasonProduct
from django.contrib import admin
from django.contrib.auth.models import Group

# Register your models here.

admin.site.site_header = "Ecommerce Admin"

products.productName = "product_Name"


class productsAdmin(admin.ModelAdmin):
    list_display = ("productName", "catName")


admin.site.register(products, productsAdmin)
admin.site.register(category)
admin.site.register(subCat)
admin.site.register(seasonProduct)
admin.site.register(dailyDeals)
admin.site.unregister(Group)
