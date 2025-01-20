import random
from .constants import GENRES_MODES, DEFAULT_PROGRESSION, NOTES, MODE_STEPS, CHORD_TYPES, ROMAN_TO_DEGREE

def generate_progression(tonic, genre, num_chords):
    mode = GENRES_MODES.get(genre)
    progression_template = DEFAULT_PROGRESSION.get(genre, "I - IV - V").split(" - ")
    scale = generate_scale(tonic, mode)
    chords = [
        get_chord_from_scale(scale, ROMAN_TO_DEGREE[symbol], symbol)
        for symbol in progression_template
    ]
    return {
        "tonic": tonic,
        "mode": mode,
        "progression": progression_template,
        "chords": chords[:num_chords],  # Adjust length to num_chords
    }

def generate_scale(tonic, mode):
    tonic_index = NOTES.index(tonic)
    steps = MODE_STEPS.get(mode, MODE_STEPS["Ionian"])
    return [NOTES[(tonic_index + step) % 12] for step in steps]

def get_chord_from_scale(scale, degree, chord_symbol):
    base_note = scale[degree - 1]
    chord_type = CHORD_TYPES.get(chord_symbol, "major")
    return f"{base_note} ({chord_type})"
