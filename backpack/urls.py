from django.urls import path
from . import views

app_name = 'backpack'

urlpatterns = [
    path('view/', views.view_backpack, name='view_backpack'),
    path('checkout/', views.checkout, name='checkout'),
    path('complete/', views.complete_purchase, name='complete_purchase'),
    path('remove/<int:game_id>', views.remove_from_backpack, name='remove_from_backpack')
]