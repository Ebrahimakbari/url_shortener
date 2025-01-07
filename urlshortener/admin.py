from django.contrib import admin
from .models import UrlShortener
# Register your models here.



@admin.register(UrlShortener)
class UrlShortenerAdmin(admin.ModelAdmin):
    list_display = ['original_url', 'short_url', 'created', 'times_used']