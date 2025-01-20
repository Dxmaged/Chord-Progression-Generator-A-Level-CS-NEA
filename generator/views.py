from django.shortcuts import render

from . models import Keys

# Create your views here.

def homepage(request):
    generator = generator.objects.all()

    context = {"generator":generator}
    return render(request, "generator/homepage.html", context)