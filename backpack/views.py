from django.shortcuts import redirect, render
from django.contrib import messages
from discover.models import Game

def remove_from_backpack(request, game_id):
    # Ensure there's a backpack list in session
    if 'backpack' not in request.session:
        request.session['backpack'] = []

    if game_id in request.session['backpack']:
        request.session['backpack'].remove(game_id)
        request.session.modified = True
        messages.success(request, "Game removed from your backpack.")
    else:
        messages.warning(request, "Game was not found in your backpack.")
    
    return redirect('backpack:view_backpack')

def view_backpack(request):
    game_ids = request.session.get('backpack', [])
    games = Game.objects.filter(id__in=game_ids)
    return render(request, 'backpack/view_backpack.html', {'games': games})