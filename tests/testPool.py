import unittest
from main import Pool


class TestPool(unittest.TestCase):

    def test_pool_exists(self):
        self.assertIsNotNone(Pool)

    def test_pool_list_exist(self):
        pool = Pool()
        self.assertIsNotNone(pool.pool)

    def sqe(self):
        print()