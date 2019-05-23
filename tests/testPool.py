import unittest
from main import Pool


class TestPool(unittest.TestCase):

    # EXISTING
    def test_pool_exists(self):
        self.assertIsNotNone(Pool)

    def test_variants_list_exists(self):
        pool = Pool()
        self.assertEqual(pool.variants, [])

    def test_music_list_exists(self):
        pool = Pool()
        self.assertEqual(pool.music, [])

    def test_current_music_exists(self):
        pool = Pool()
        self.assertEqual(pool.current_music, -1)

    def test_play_music(self):
        pool = Pool()
        pool.add_music('../music/lazzyTown.wav', 'Super Ice - We are number one')
        pool.set_random_current_music()
        pool.play_music()
        self.assertEqual(1, 1)

    # LOGIC
    def test_set_random_current_music(self):
        pool = Pool()
        pool.add_music('../music/lazzyTown.wav', 'Super Ice - We are number one')
        pool.set_random_current_music()
        self.assertGreaterEqual(pool.current_music, 0)

    def test_valid_current_music(self):
        pool = Pool()
        pool.set_random_current_music()
        self.assertEqual(pool.current_music, -1)

    def test_add_music(self):
        pool = Pool()
        pool.add_music('../music/lazzyTown.wav', 'Super Ice - We are number one')
        self.assertEqual(pool.music, ['../music/lazzyTown.wav'])

    def test_add_variant(self):
        pool = Pool()
        pool.add_variant('new var')
        self.assertEqual(pool.variants, ['new var'])


    def test_check_choice(self):
        pool = Pool()
        pool.add_music('../music/lazzyTown.wav', 'Super Ice - We are number one')
        pool.set_random_current_music()
        result = pool.check_choice(1)
        self.assertEqual(result, 1)