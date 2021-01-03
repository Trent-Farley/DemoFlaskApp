class DuplicateCounter:

    def __init__(self, duplicates: list) -> None:
        self.list = duplicates

    def __add__(self, other) -> None:
        for num in other.list:
            self.list.append(num)

    def count_duplicates(self) -> int:
        if not self.list:
            raise TypeError("Duplicates must be in a list")

        count = 0
        new_list = []

        for i in self.list:
            if i not in new_list:
                new_list.append(i)
            else:
                count += 1

        return count