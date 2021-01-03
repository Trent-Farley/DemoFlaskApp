class DuplicateRemover:
    def __init__(self, duplicates: list) -> None:
        self.list = duplicates

    def __add__(self, other) -> None:
        for num in other.list:
            self.list.append(num)

    def remove_duplicates(self) -> list:
        if not self.list:
            raise TypeError("duplicates must be in a list")

        new_list = []

        for i in self.list:
            if i not in new_list:
                new_list.append(i)

        return new_list