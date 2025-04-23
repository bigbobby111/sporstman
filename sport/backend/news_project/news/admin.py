from django.contrib import admin
from .models import NewsItem

@admin.register(NewsItem)
class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'time', 'is_slider')
    list_filter = ('category', 'is_slider')
    search_fields = ('title', 'description')
