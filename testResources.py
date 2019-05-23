import unittest
import pyglet

class TestResourcesExisting(unittest.TestCase):
    def test_pyglet_not_install(self):
        self.assertIsNotNone(pyglet, "pyglet cant be None")

    def test_lazzy_town_music(self):
        music = pyglet.media.load('music/lazzyTown.mp3')
        self.assertIsNotNone(music, 'music/lazzyTown.mp3 must exists')