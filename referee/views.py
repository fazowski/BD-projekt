from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.urls import reverse_lazy
from django.db import connection

from .models import Team, Match

class ManagerIndexView(LoginRequiredMixin, generic.ListView):
    """
    View class for home page
    """
    template_name = 'index.html'
    model = Match
    context_object_name = 'match_list'
    queryset = Match.objects.all()

###########################################################
#
# Teams Views
#
##########################################################
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


###########################################################
#
# Matches Views
#
###########################################################
class MatchListView(LoginRequiredMixin, generic.ListView):
    """
    View class for team list
    """
    model = Match
    context_object_name = 'match_list'
    queryset = Match.objects.all()


def match_details_view(request, match_id):
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM V_MATCH_DETAILS WHERE MATCH_ID = {0}".format(match_id))
        row = cursor.fetchone()

        columns = [col[0] for col in cursor.description]
        # print(dict(zip(columns, row)))
        context = {
            'match': dict(zip(columns, row))
        }

        return render(request, 'referee/match_detail.html', context)