from django.shortcuts import render
from .chord_generator import generate_progression  
from .constants import NOTES, GENRES_MODES  
import json

def homepage(request):
    # Static data
    notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]
    genres = ["Pop", "Jazz", "Blues", "Flamenco", "Middle Eastern", "Dreamy", "Rock", "Ballad", "Experimental"]
    
    # Default values
    instrument = "guitar"  # Default instrument
    progression_data = None

    if request.method == "POST":
        # Handle Chord Progression Generator form
        if "tonic" in request.POST:
            tonic = request.POST.get("tonic")
            genre = request.POST.get("genre")
            num_chords = int(request.POST.get("num_chords", 4))  # Default to 4 if not provided
            progression_data = generate_progression(tonic, genre, num_chords)
        
        # Handle Instrument Selection form
        if "instrument" in request.POST:
            instrument = request.POST.get("instrument")

    context = {
        "notes": notes,
        "genres": genres,
        "notes_json": json.dumps(notes),
        "genres_json": json.dumps(genres),
        'progression_data': progression_data,
        'instrument': instrument,
    }
    # Render the template with all required data
    return render(request, "homepage.html", context)

def help_view(request):
    return render(request, "help.html")