class ChristmasTree:

    def size(self, size: int) -> str:
        tree = ""

        for layer in range(size):
            tree += (" " * (size - layer - 1))
            tree += ("X" * (layer * 2 + 1))
            tree += "\n"

        tree += (" " * (size - 1))
        tree += "|"

        return tree
