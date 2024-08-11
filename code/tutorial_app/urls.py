from django.urls import path 
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('player/', views.player_view, name='player'),
    path('jury/', views.jury_view, name='jury'),
    path('coach/', views.coach_view, name='coach'),
    path('dbmanager/', views.dbmanager_view, name='dbmanager'),
    path('add_player/', views.add_player_view, name='add_player'),
    path('add_jury/', views.add_jury_view, name='add_jury'),
    path('add_coach/', views.add_coach_view, name='add_coach'),
    path('update_stadium/', views.update_stadium_view, name='update_stadium'),
    path('delete_session/', views.delete_session_view, name='delete_session'),
    path('list_stadium/', views.list_stadium_view, name='list_stadium'),
    path('average_rating/', views.average_rating_view, name='average_rating'),
    path('list_player/', views.list_player_view, name='list_player'),
    path('average_height/', views.average_height_view, name='average_height'),
    path('add_new_session/', views.add_new_session_view, name='add_new_session'),
    path('rate_session/', views.rate_session_view, name='rate_session'),
    path('squad/', views.squad_view, name='squad'),
]