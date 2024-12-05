from django.shortcuts import render
from .models import Game

def discover(request):
    """
    Render the Discover page, allowing visitors to browse available games.
    """
    games = Game.objects.all().order_by('title')
    return render(request, 'discover/discover.html', {'games': games})