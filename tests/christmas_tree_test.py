import unittest

from src.christmas_tree import ChristmasTree


class ChristmasTreeTest(unittest.TestCase):

    def test_tree_of_size_0(self):
        tree = ChristmasTree()

        self.assertEqual(tree.size(0), '|')

    def test_tree_of_size_1(self):
        tree = ChristmasTree()
        expected = (
            "X\n"
            "|"
        )

        self.assertEqual(tree.size(1), expected)

    def test_tree_of_size_2(self):
        tree = ChristmasTree()
        expected = (
            " X\n"
            "XXX\n"
            " |"
        )

        self.assertEqual(tree.size(2), expected)
