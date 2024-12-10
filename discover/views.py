from django.shortcuts import render
from .models import Game

def discover(request):
    """
    Render the Discover page, allowing visitors to browse available games.
    Filters by genre, platform, and release_date range.
    """
    games = Game.objects.all().order_by('title')

    # Get distinct genres and platforms for dropdowns
    genres = Game.objects.values_list('genre', flat=True).distinct().order_by('genre')
    platforms = Game.objects.values_list('platform', flat=True).distinct().order_by('platform')

    # Get filter parameters
    selected_genre = request.GET.get('genre', '')
    selected_platform = request.GET.get('platform', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')

    # Apply filters
    if selected_genre:
        games = games.filter(genre=selected_genre)
    if selected_platform:
        games = games.filter(platform=selected_platform)
    if date_from:
        games = games.filter(release_date__gte=date_from)
    if date_to:
        games = games.filter(release_date__lte=date_to)

    context = {
        'games': games,
        'genres': genres,
        'platforms': platforms,
        'request': request,  # Pass request to template for easy GET retrieval
    }
    return render(request, 'discover/discover.html', context)
