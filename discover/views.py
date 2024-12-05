from django.shortcuts import render

def discover(request):
    """
    Render the Discover page, allowing visitors to browse available games.
    """
    return render(request, 'discover/discover.html')