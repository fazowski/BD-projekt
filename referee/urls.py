from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManagerIndexView.as_view(), name='index'),
    # Teams URLs
    path('teams', views.TeamListView.as_view(), name='teams'),
    path('teams/add', views.TeamCreateView.as_view(), name='team_add'),
    path('teams/edit/<int:pk>', views.TeamUpdateView.as_view(), name='team_edit'),
    path('teams/delete/<int:pk>', views.TeamDeleteView.as_view(), name='team_delete'),
    path('teams/details/<int:pk>', views.TeamDetailView.as_view(), name='team_detail'),
    # Matches URLs
    path('matches', views.MatchListView.as_view(), name='matches'),
]