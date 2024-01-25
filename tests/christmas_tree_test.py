import unittest

from src.christmas_tree import ChristmasTree


class ChristmasTreeTest(unittest.TestCase):

    def test_tree_of_size_0(self):
        tree = ChristmasTree()

        self.assertEqual(tree.size(0), '|')
