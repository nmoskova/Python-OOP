class vowels:
    def __init__(self, some_string: str):
        self.some_string = some_string
        self.vowels = "AEIOUYaeiouy"
        self.vowels_list = [el for el in self.some_string if el in self.vowels]
        self.start_idx = 0
        self.end_idx = len(self.vowels_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.start_idx == self.end_idx:
            raise StopIteration

        curr_idx = self.start_idx
        self.start_idx += 1
        return self.vowels_list[curr_idx]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
