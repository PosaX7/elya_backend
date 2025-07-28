# stats/admin.py
from django.contrib import admin
from .models import Stat

@admin.register(Stat)
class StatAdmin(admin.ModelAdmin):
    list_display = ['user', 'content_type', 'content_id', 'action', 'timestamp']
    list_filter = ['content_type', 'action', 'timestamp']
