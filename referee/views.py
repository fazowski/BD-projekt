from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
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