import unittest
import pyglet
import main

class TestChoseMusic(unittest.TestCase):
    def test_make_choice_exists(self):
        choice = main.makeChoice()
        self.assertIsNotNone(choice, 'makeChoice func must be existing')
