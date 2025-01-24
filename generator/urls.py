from django.urls import path, include

from . import views

app_name = "generator"

urlpatterns = [
    path("", views.homepage, name="homepage"),

]