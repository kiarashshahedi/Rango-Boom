from django.contrib import admin
from .models import Category, Product
from django.utils.safestring import mark_safe


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_category', 'icon_preview')
    list_filter = ('parent_category',)
    search_fields = ('name',)
    fields = ('name', 'parent_category', 'icon', 'icon_preview')
    readonly_fields = ('icon_preview',)

    def icon_preview(self, obj):
        if obj.icon:
            return mark_safe(f'<img src="{obj.icon.url}" style="width: 50px; height: 50px;" />')
        return "No Icon"

    icon_preview.short_description = "Icon Preview"

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['name', 'description']
    ordering = ['-created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
