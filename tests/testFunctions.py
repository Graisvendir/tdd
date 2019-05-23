import unittest
import main

class TestChoseMusic(unittest.TestCase):
    def setUp(self) -> None:
        self.choice = main.makeChoice()

    def test_make_choice_exists(self):
        self.assertIsNotNone(self.choice, 'makeChoice func must be existing')

    def test_choice_is_int(self):
        self.assertTrue(isinstance(self.choice, int))
