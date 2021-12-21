class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = 0
        self.current_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count == self.count:
            raise StopIteration

        current_num = self.start
        self.start += self.step
        self.current_count += 1
        return current_num


numbers = take_skip(2, 6)
for number in numbers:
    print(number)


numbers = take_skip(10, 5)
for number in numbers:
    print(number)
