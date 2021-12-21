class reverse_iter:
    def __init__(self, some_iterable):
        self.some_iterable = some_iterable
        self.start = len(self.some_iterable) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration

        current_item = self.some_iterable[self.start]
        self.start -= 1
        return current_item


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
      