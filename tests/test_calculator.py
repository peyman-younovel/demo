import unittest
import sys
from pathlib import Path

# Adjust the path to include the src directory
sys.path.append(str(Path(__file__).parent.parent / 'src'))

from calculator import add

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3)

if __name__ == "__main__":
    unittest.main()
    