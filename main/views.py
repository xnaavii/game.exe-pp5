from django.shortcuts import render


def landing_page(request):
    """
    Render the landing page for the Game.exe platform.

    This page provides an introduction to the platform and directs visitors
    to explore games or log in.

    """
    return render(request, 'main/landing_page.html')


def custom_404(request, exception):
    """
    Render a custom 404 page when a requested page is not found.

    """
    return render(request, 'main/404.html', status=404)
