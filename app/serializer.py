from rest_framework import serializers
from .models import *

class OccassionalCakesSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name')
    category_slug = serializers.CharField(source='category.slug')
    category_id = serializers.IntegerField(source='category.id')
    class Meta:
        model = OccassionalCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'is_available','category_name','category_slug','category_id']


class WeddingCakesSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeddingCakes
        fields = ['id', 'name', 'slug', 'image', 'image2', 'image3', 'description','price', 'range_price', 'is_available']


class CategorySerializer(serializers.ModelSerializer):
    products = WeddingCakesSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'products']

class BlogsSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='blog_category.name')
    category_slug = serializers.CharField(source='blog_category.slug')
    category_id = serializers.IntegerField(source='blog_category.id')
    class Meta:
        model = Blogs
        fields = ['id', 'image', 'heading', 'created_at', 'text','tex2','text3','category_name','category_slug', 'category_id']

class BlogCategorySerializer(serializers.ModelSerializer):
    blogs = BlogsSerializer(many=True, read_only=True)
    class Meta:
        model = Category
        fields = ['id', 'name', 'slug', 'blogs']