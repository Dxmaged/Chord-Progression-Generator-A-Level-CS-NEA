from django.urls import path, include

from .views import homepage

app_name = "keys"

urlpatterns = [
    path("", homepage, name="home"),
]