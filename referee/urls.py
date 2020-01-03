from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManagerIndexView.as_view(), name='index'),
    path('teams', views.TeamListView.as_view(), name='teams'),
    path('teams/details/<int:pk>', views.TeamDetailView.as_view(), name='team_detail'),
]