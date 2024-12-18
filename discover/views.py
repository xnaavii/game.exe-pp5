from django.shortcuts import render, get_object_or_404, redirect
from .models import Game, Platform
from django.contrib import messages

CONSOLE_LINKS = {
    'PS5': 'https://www.playstation.com',
    'Xbox': 'https://www.xbox.com',
    'Switch': 'https://www.nintendo.com',
}

def discover(request):
    """
    Render the Discover page, allowing visitors to browse available games.
    Filters by genre, platform, and release_date range.
    """
    games = Game.objects.all().order_by('title')

    # Get distinct genres and platforms for dropdowns
    genres = Game.objects.values_list('genre', flat=True).distinct().order_by('genre')
    platforms = Platform.objects.values_list('name', flat=True).order_by('name')

    # Get filter parameters
    selected_genre = request.GET.get('genre', '')
    selected_platform = request.GET.get('platform', '')
    date_from = request.GET.get('date_from', '')
    date_to = request.GET.get('date_to', '')
    search_query = request.GET.get('search', '')


    # Apply filters
    if selected_genre:
        games = games.filter(genre=selected_genre)
    if selected_platform:
        games = games.filter(platforms__name=selected_platform)
    if date_from:
        games = games.filter(release_date__gte=date_from)
    if date_to:
        games = games.filter(release_date__lte=date_to)
    # Apply Search Filter
    if search_query:
        games = games.filter(title__icontains=search_query)

    context = {
        'games': games,
        'genres': genres,
        'platforms': platforms,
        'request': request,  # Pass request to template for easy GET retrieval
    }
    return render(request, 'discover/discover.html', context)


def game_detail(request, game_id):
    """
    Display detailed information about a specific game, including title, price, genre,
    platforms, release date, rating, description, and a form to purchase based on platform.
    """
    game = get_object_or_404(Game, id=game_id)
    platforms = game.platforms.all()  # Retrieve all associated platforms

    return render(request, 'discover/game_detail.html', {
        'game': game,
        'platforms': platforms,
    })

def purchase_game(request, game_id):
    """
    Handle the purchase form from the game detail page.
    If PC is selected, add the game to the backpack.
    Otherwise, redirect to the external platform site if available.
    """
    game = get_object_or_404(Game, id=game_id)
    selected_platform = request.POST.get('platform_choice', '')

    if selected_platform == 'PC':
        # Add to backpack (session-based)
        if 'backpack' not in request.session:
            request.session['backpack'] = []
        if game_id not in request.session['backpack']:
            request.session['backpack'].append(game_id)
            request.session.modified = True
            messages.success(request, f"{game.title} (PC) has been added to your backpack.")
        else:
            messages.warning(request, f"{game.title} (PC) is already in your backpack.")
        return redirect('discover:game_detail', game_id=game_id)
    else:
        # Check if console platform is known
        if selected_platform in CONSOLE_LINKS:
            return redirect(CONSOLE_LINKS[selected_platform])
        else:
            messages.error(request, "Unknown platform selected or platform not supported.")
            return redirect('discover:game_detail', game_id=game_id)