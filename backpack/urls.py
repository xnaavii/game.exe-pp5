from django.urls import path
from . import views

app_name = 'backpack'

urlpatterns = [
    path('add/<int:game_id>/', views.add_to_backpack, name='add_to_backpack'),
    path('view/', views.view_backpack, name='view_backpack'),
]