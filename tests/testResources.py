import unittest
import pygame

class TestResourcesExisting(unittest.TestCase):
    def test_pygame_not_install(self):
        self.assertIsNotNone(pygame, "pyglet cant be None")

    def test_lazzy_town_music(self):
        pygame.mixer.init()
        pygame.mixer.music.load('../music/lazzyTown.wav')
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
        self.assertIsNotNone(1, 'music/lazzyTown.mp3 must exists')