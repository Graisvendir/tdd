import unittest
import pyglet
import main

class TestChoseMusic(unittest.TestCase):
    def testMakeChoiceExists(self):
        choice = main.makeChoice()
        self.assertIsNotNone(choice, 'makeChoice func must be existing')