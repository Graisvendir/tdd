import unittest
import pyglet

class TestChoseMusic(unittest.TestCase):
    def testPygletNotInstall(self):
        self.assertIsNotNone(pyglet, "pyglet cant be None")