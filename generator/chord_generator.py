import random
from .constants import GENRES_MODES, DEFAULT_PROGRESSION, NOTES, MODE_STEPS, CHORD_TYPES, ROMAN_TO_DEGREE

def generate_progression(tonic, genre, num_chords):
    mode = GENRES_MODES.get(genre)
    # Randomly select a progression for the genre
    progression_template = random.choice(DEFAULT_PROGRESSION.get(genre, ["I - IV - V"]))
    progression_template = progression_template.split(" - ")
    
    # Repeat the progression to match or exceed the desired number of chords
    repeated_template = (progression_template * ((num_chords // len(progression_template)) + 1))[:num_chords]
    
    scale = generate_scale(tonic, mode)
    chords = [
        get_chord_from_scale(scale, ROMAN_TO_DEGREE[symbol], symbol)
        for symbol in repeated_template
    ]
    
    return {
        "tonic": tonic,
        "mode": mode,
        "progression": repeated_template,
        "chords": chords,  # Return the full repeated chords
    }


def generate_scale(tonic, mode):
    # Get the index of the tonic note in the NOTES list
    tonic_index = NOTES.index(tonic)
    
    # Retrieve the steps for the given mode (default to Ionian if mode is unknown)
    steps = MODE_STEPS.get(mode, MODE_STEPS["Ionian"])
    
    # Generate the scale by applying mode steps to the tonic note
    return [NOTES[(tonic_index + step) % 12] for step in steps]

def get_chord_from_scale(scale, degree, chord_symbol):
    base_note = scale[degree - 1]  # Find the root note of the chord
    chord_type = CHORD_TYPES.get(chord_symbol, "major")  # Determine the chord type (default to major)
    return f"{base_note} ({chord_type})"  # Return chord notation
