from django.contrib import admin
from service.models import Features
from category.models import Category
class FeaturesAdmin(admin.ModelAdmin):
    list_display =('Features_name','Features_price','Features_desc','Features_img')
admin.site.register(Features,FeaturesAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display =('Category_name','Category_desc','Category_img')
admin.site.register(Category,CategoryAdmin)

