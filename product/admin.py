from django.contrib import admin

from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = ('title',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'img', 'price', )
    list_filter = ('title', 'category', 'price')
    search_fields = ('title', 'category', 'price')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
