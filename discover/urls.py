from django.urls import path
from . import views

app_name = 'discover'

urlpatterns = [
    path('', views.discover, name='discover'),
    path('game/<int:game_id>/', views.game_detail, name='game_detail'),
]