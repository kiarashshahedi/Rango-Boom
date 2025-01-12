from rest_framework import serializers
from .models import Product, Category

class CategorySerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = ['id', 'name', 'parent_category', 'children']

    def get_children(self, obj):
        children = Category.objects.filter(parent_category=obj.name)
        return CategorySerializer(children, many=True).data


        
class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # Nested category details

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'stock', 'image', 'category', 'created_at', 'updated_at']
