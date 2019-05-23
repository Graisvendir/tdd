import unittest
from main import Pool


class TestPool(unittest.TestCase):

    # EXISTING
    def test_pool_exists(self):
        self.assertIsNotNone(Pool)

    def test_variants_list_exist(self):
        pool = Pool()
        self.assertIsNotNone(pool.variants)

    def test_music_list_exist(self):
        pool = Pool()
        self.assertIsNotNone(pool.music)

    # LOGIC
    def test_add_music(self):
        pool = Pool()
        pool.add_music('music/lazzyTown.mp3')
        self.assertEqual(pool.music, ['music/lazzyTown.mp3'])

    def test_add_variant(self):
        pool = Pool()
        pool.add_variant('new var')
        self.assertEqual(pool.variants, ['new var'])
