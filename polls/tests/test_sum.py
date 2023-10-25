from ..views import sum
import unittest

# Create your tests here.
class TestBasic(unittest.TestCase):
    "Basic tests"

    def test_basic(self):
        a = 1
        b = 2
        self.assertEqual(a+b, sum(a, b))