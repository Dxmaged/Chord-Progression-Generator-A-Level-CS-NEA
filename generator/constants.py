GENRES_MODES = {
  "Pop": "Ionian",
  "Jazz": "Dorian",
  "Blues": "Dorian",
  "Flemenco": "Phrygian",
  "Middle Eastern": "Phrygian",
  "Dreamy": "Lydian",
  "Rock": "Mixolydian",
  "Ballad": "Aeolian",
  "Experimental": "Locrian",
}

DEFAULT_PROGRESSION = {
  "Pop": "I - V - vi - IV",
  "Jazz": "ii - V - I",
  "Blues": "I - IV - V",
  "Flemenco": "i - ♭II - ♭III",
  "Middle Eastern": "i - ♭II - ♭VII",
  "Dreamy": "I - II - V - I",
  "Rock": "I - IV - V - ♭VII",
  "Ballad": "i - VI - III - VII",
  "Experimental": "i° - ♭II - iv",
}

NOTES = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

MODE_STEPS = {
  "Ionian": [0, 2, 4, 5, 7, 9, 11],
  "Dorian": [0, 2, 3, 5, 7, 9, 10],
  "Phrygian": [0, 1, 3, 5, 7, 8, 10],
  "Lydian": [0, 2, 4, 6, 7, 9, 11],
  "Mixolydian": [0, 2, 4, 5, 7, 9, 10],
  "Aeolian": [0, 2, 3, 5, 7, 8, 10],
  "Locrian": [0, 1, 3, 5, 6, 8, 10],
}

CHORD_TYPES = {
  "I": "major",
  "ii": "minor",
  "iii": "minor",
  "IV": "major",
  "V": "major",
  "vi": "minor",
  "vii°": "diminished",
  "i": "minor",
  "♭II": "major",
  "♭III": "major",
  "♭VII": "major",
}

#ROMAN_TO_DEGREE = {
#  "I": 1, "ii": 2, "iii": 3, "IV": 4, "V": 5, "vi": 6, "vii°": 7,
#  "i": 1, "♭II": 2, "♭III": 3, "♭VII": 7, "iv": 4, "i°": 1,
#}

ROMAN_TO_DEGREE = {
  "I":1, "i":1, "II":2, "ii":2, "♭II": 2, "III":3, "iii": 3, "♭III": 3,
  "IV": 4, "iv": 4, "V":5, "v":5, "VI":6, "vi":6, "vii°": 7, "♭VII": 7,
}
TONES = {
    ("Major","Major"),
    ("Minor","Minor"),
}