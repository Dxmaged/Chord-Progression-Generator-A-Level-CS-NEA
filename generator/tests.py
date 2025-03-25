from django.test import TestCase
from generator.chord_generator import generate_progression

class ChordGeneratorTests(TestCase):
    def test_generate_progression_returns_dict(self):
        result = generate_progression("C", "Jazz", 4)

    def test_generate_progression_contains_expected_keys(self):
        result = generate_progression("C", "Jazz", 4)


    def test_generate_progression_generates_correct_number_of_chords(self):
        num_chords = 4
        result = generate_progression("C", "Jazz", num_chords)

