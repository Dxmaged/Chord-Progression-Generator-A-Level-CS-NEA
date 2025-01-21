from django.shortcuts import render
from .chord_generator import generate_progression  

def homepage(request):
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    genres = ["Pop", "Jazz", "Blues", "Flamenco", "Middle Eastern", "Dreamy", "Rock", "Ballad", "Experimental"]
    
    if request.method == "POST":
        tonic = request.POST.get("tonic")
        genre = request.POST.get("genre")
        num_chords = int(request.POST.get("num_chords", 4))  # Default to 4 if not provided
        progression_data = generate_progression(tonic, genre, num_chords)
        return render(request, "homepage.html", {"progression_data": progression_data, "notes": notes, "genres": genres})
    
    return render(request, "homepage.html", {"notes": notes, "genres": genres})

