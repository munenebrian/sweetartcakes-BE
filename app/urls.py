from django.urls import path
from app import views

urlpatterns = [
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogcategories/', views.api_blogscategories, name='apiBlogCategories' ),
    path('getBlogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('categoryblogs/<int:blogcategory_id>/', views.getBlogByCategory, name='apiCategoryblogs' ),
    path('weddingcakes/', views.weddingCakes, name='weddingcakes' ),
    path('weddingcakedetails/<int:product_id>/', views.weddingCakeDetails, name='weddingCakeDetails' ),
    path('occassionalcakes/', views.occassionalCakes, name='occassionalCakes' ),
    path('categories/', views.api_categories, name='apiCategories' ),
    path('occassionalcakedetails/<int:product_id>/', views.occassionalCakeDetails, name='occassionalCakeDetails' ),
    path('categoryoccassionalcakes/<int:category_id>/', views.getoccassionalCakesByCategory, name='getoccassionalCakesByCategory' ),
]
