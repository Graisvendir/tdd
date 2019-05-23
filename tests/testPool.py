import unittest
from main import Pool


class TestPool(unittest.TestCase):

    def test_pool_exists(self):
        self.assertIsNotNone(Pool)

    def sqe(self):
        print()