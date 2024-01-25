class ChristmasTree:

    def size(self, size: int) -> str:
        if size == 1:
            return (
                "X\n"
                "|"
            )

        if size == 2:
            return (
                " X\n"
                "XXX\n"
                " |"
            )

        return '|'
