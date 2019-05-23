import unittest
from main import Pool

class TestPool(unittest.TestCase):
    def poolExists(self):
        self.assertIsNotNone(Pool)