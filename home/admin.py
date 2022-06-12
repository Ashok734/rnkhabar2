from django.contrib import admin
from .models import Category, News
# Register your models here.
class AdminNews(admin.ModelAdmin):
    list_display = ('image_post', 'title', 'category', 'add_time')
    list_filter = ('category',)
    list_per_page = 10


admin.site.register(Category)

admin.site.register(News, AdminNews)

