from django.contrib import admin
from .models import Game, Platform

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'genre', 'release_date', 'rating',)

@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name',)