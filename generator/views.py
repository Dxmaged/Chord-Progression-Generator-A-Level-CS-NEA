from django.shortcuts import render



# Create your views here.

def homepage(request):
    generator = generator.objects.all()

    context = {"generator":generator}
    return render(request, "generator/homepage.html", context)