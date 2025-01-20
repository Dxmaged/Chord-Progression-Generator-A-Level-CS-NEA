from django.urls import path, include

app_name = "generator"

from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),

]