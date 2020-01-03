from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin


from .models import Match


class ManagerIndexView(LoginRequiredMixin, generic.ListView):
    """
    View class for home page
    """
    template_name = 'index.html'
    model = Match
    context_object_name = 'match_list'
    queryset = Match.objects.all()


