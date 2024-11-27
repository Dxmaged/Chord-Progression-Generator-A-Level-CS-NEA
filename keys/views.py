from django.shortcuts import render

from . models import Keys
# Create your views here.

def homepage(request):
    keys = Keys.objects.all()

    context = {"keys":keys}
    return render(request, "keys/homepage.html", context)
