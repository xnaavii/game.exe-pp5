from django.contrib import admin
from .models import Game

@admin.register(Game)
class GameAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'genre', 'platform', 'release_date', 'rating')
    search_fields = ('title', 'genre', 'platform')
    list_filter = ('genre', 'platform', 'release_date')