from django.urls import path
from app import views

urlpatterns = [
    path('', views.productsPage, name='productsPage'),
    path('emails/', views.send_mail, name='email'),
    path('blogs/', views.get_blogs, name='blogs'),
    path('blogcategories/', views.api_blogscategories, name='apiBlogCategories' ),
    path('getBlogDetails/<int:blog_id>/', views.getBlogDetails, name='Blog Details' ),
    path('categoryblogs/<int:blogcategory_id>/', views.getProductsByCategory, name='apiCategoryblogs' ),
    path('products/', views.api_products, name='apiProducts' ),
    path('categories/', views.api_categories, name='apiCategories' ),
    path('getProductDetails/<int:product_id>/', views.getProductDetails, name='getProductDetails' ),
    path('categoryproducts/<int:category_id>/', views.getProductsByCategory, name='apiCategoryproducts' ),
    path('services/', views.get_services, name='services'),
    path('getServiceDetails/<int:service_id>/', views.getServiceDetails, name='Service Details' ),
]