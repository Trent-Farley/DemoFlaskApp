import unittest
from duplicateRemover import DuplicateRemover
from duplicateCounter import DuplicateCounter


class TestDuplicateRemover(unittest.TestCase):
    def testRemover(self):
        duplicates = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
        duplicate_remover = DuplicateRemover(duplicates)
        expected = [1, 2, 3, 4, 5]
        result = duplicate_remover.remove_duplicates()
        self.assertEqual(expected, result)

class TestCountDuplicares(unittest.TestCase):
    def test_Counter(self):
        duplicates = [1, 1, 1, 2, 2, 3, 3, 4, 4, 4, 5, 5, 5]
        duplicate_counter = DuplicateCounter(duplicates)
        expected = 8
        result = duplicate_counter.count_duplicates()
        self.assertEqual(expected, result)

if __name__ == '__main__':
    unittest.main()