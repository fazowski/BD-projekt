from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy

from .models import Team
from .models import Match


class ManagerIndexView(LoginRequiredMixin, generic.ListView):
    """
    View class for home page
    """
    template_name = 'index.html'
    model = Match
    context_object_name = 'match_list'
    queryset = Match.objects.all()

"""
    TEAMS
"""


class TeamListView(LoginRequiredMixin, generic.ListView):
    """
    View class for team list
    """
    model = Team
    context_object_name = 'team_list'
    queryset = Team.objects.all()


class TeamDetailView(LoginRequiredMixin, generic.DetailView):
    """
    View class for team detail page
    """
    model = Team


class TeamCreateView(LoginRequiredMixin, PermissionRequiredMixin, generic.CreateView):
    """
        View class for adding team
    """
    permission_required = 'teams.can_modify_team'
    model = Team
    fields = '__all__'
    success_url = reverse_lazy('teams')


class TeamUpdateView(LoginRequiredMixin, PermissionRequiredMixin, generic.UpdateView):
    """
        View class for editing team
    """
    permission_required = 'teams.can_modify_team'
    model = Team
    fields = '__all__'
    success_url = reverse_lazy('teams')


class TeamDeleteView(LoginRequiredMixin, PermissionRequiredMixin, generic.DeleteView):
    """
        View class for deleting team
    """
    permission_required = 'teams.can_modify_team'
    model = Team
    success_url = reverse_lazy('teams')
