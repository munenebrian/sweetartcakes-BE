from django.contrib import admin

from app.models import *

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class BlogCategoryAdmin(admin.ModelAdmin):
    list_display = ('name','slug')
    prepopulated_fields = {'slug': ('name',)}

class OccassionalCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price','category', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

class WeddingCakesAdmin(admin.ModelAdmin):
    list_display = ('name', 'new_price', 'old_price', 'is_available')
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(OccassionalCakes, OccassionalCakesAdmin )
admin.site.register(WeddingCakes, WeddingCakesAdmin )
admin.site.register(Category, CategoryAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)
admin.site.register(Blogs)