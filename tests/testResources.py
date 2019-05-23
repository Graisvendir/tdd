import unittest
import os
import pygame

class TestResourcesExisting(unittest.TestCase):
    def test_pygame_not_install(self):
        self.assertIsNotNone(pygame, "pygame cant be None")

    def test_lazzy_town_music(self):
        path = '../music/lazzyTown.wav'
        self.assertTrue(os.path.exists(path))

    def test_back_in_black_music(self):
        path = '../music/BackInBlack.wav'
        self.assertTrue(os.path.exists(path))
