from django.urls import path
from . import views

app_name = 'discover'

urlpatterns = [
    path('', views.discover, name='discover'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
    path('game/<int:game_id>/purchase/', views.purchase_game, name='purchase_game'),
]