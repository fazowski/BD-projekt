from django.urls import path
from . import views

urlpatterns = [
    path('', views.ManagerIndexView.as_view(), name='index')
]