from django.contrib import admin
from .models import Category, Product


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'get_parent_category_display']  # Use the display name of the choice field
    list_filter = ['parent_category']  # Django can filter choice fields directly

    def get_parent_category_display(self, obj):
        return obj.get_parent_category_display()  # This will display the human-readable value
    get_parent_category_display.short_description = 'دسته‌بندی والد'


class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'stock', 'category', 'created_at']
    list_filter = ['category']
    search_fields = ['name', 'description']
    ordering = ['-created_at']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
