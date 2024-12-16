from django.shortcuts import redirect, get_object_or_404, render
from django.contrib import messages
from discover.models import Game

def add_to_backpack(request, game_id):
    game = get_object_or_404(Game, id=game_id)

    if 'backpack' not in request.session:
        request.session['backpack'] = []

    if game_id not in request.session['backpack']:
        request.session['backpack'].append(game_id)
        request.session.modified = True
        messages.success(request, f"'{game.title}' added to your backpack.")
    else:
        messages.warning(request, f"'{game.title}' is already in your backpack.")

    return redirect('discover:discover')

def view_backpack(request):
    game_ids = request.session.get('backpack', [])
    games = Game.objects.filter(id__in=game_ids)
    return render(request, 'backpack/view_backpack.html', {'games': games})