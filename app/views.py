from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Q
# from simple_mail.mail import send_mail

from app.models import *
from .serializer import *
from .pagination import *
from rest_framework import generics
from rest_framework.pagination import PageNumberPagination


# Create your views here

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000

@api_view(['GET',])
def api_categories(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def weddingCakes(request):
    if request.method == "GET":
        products = WeddingCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = WeddingCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def weddingCakeDetails(request, product_id):
    if request.method == "GET":
        product= WeddingCakes.objects.filter(id = product_id)
        serializer = WeddingCakesSerializer(product, many=True)
        return Response(serializer.data)

@api_view(['GET',])
def occassionalCakes(request):
    if request.method == "GET":
        products = OccassionalCakes.objects.all()

        # Set up pagination
        paginator = PageNumberPagination()
        paginator.page_size = 300
        result_page = paginator.paginate_queryset(products, request)

        # Serialize the result page
        serializer = OccassionalCakesSerializer(result_page, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def occassionalCakeDetails(request, product_id):
    if request.method == "GET":
        product= OccassionalCakes.objects.filter(id = product_id)
        serializer = OccassionalCakesSerializer(product, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def getoccassionalCakesByCategory(request, category_id):
    if request.method == "GET":
        category = get_object_or_404(Category, id=category_id)
        products = OccassionalCakes.objects.filter(category=category)
        serializer = OccassionalCakesSerializer(products, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_blogs(request):
    if request.method == "GET":
        blogs = Blogs.objects.all()
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET',])
def api_blogscategories(request):
    if request.method == "GET":
        blogcategories = BlogCategory.objects.all()
        serializer = BlogCategorySerializer(blogcategories, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getBlogDetails(request, blog_id):
    if request.method == "GET":
        blogs= Blogs.objects.filter(id = blog_id)
        serializer = BlogsSerializer(blogs, many=True)
        return Response(serializer.data)
    
@api_view(['GET'])
def getBlogByCategory(request, blogcategory_id):
    if request.method == "GET":
        blogcategory = get_object_or_404(BlogCategory, id=blogcategory_id)
        blogs = Blogs.objects.filter(blog_category=blogcategory)
        serializer =BlogsSerializer(blogs, many=True)
        return Response(serializer.data)