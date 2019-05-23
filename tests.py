import unittest
import pyglet
import main

class TestChoseMusic(unittest.TestCase):
    def testPygletNotInstall(self):
        self.assertIsNotNone(pyglet, "pyglet cant be None")

    def testLazzyTownMusic(self):
        music = pyglet.media.load('music/lazzyTown.mp3')
        self.assertIsNotNone(music, 'music/lazzyTown.mp3 must exists')
