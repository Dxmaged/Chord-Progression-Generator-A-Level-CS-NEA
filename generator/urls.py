from django.urls import path, include

from . import views
from .views import help_view

app_name = "generator"

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("help/", views.help_view, name="help")

]