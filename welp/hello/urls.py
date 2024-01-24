from django.urls import path
from hello import views
from django.views.generic.base import TemplateView


urlpatterns = [
    path("", views.home, name="home"),
   
]