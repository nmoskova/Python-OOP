class Stack(list):
    def __init__(self):
        super().__init__()
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        if self.data:
            return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return True if not self.data else False

    def __str__(self):
        data_reversed = ', '.join(self.data[::-1])
        return f"[{data_reversed}]"


s = Stack()
print(s.is_empty())
s.push("apple")
s.push("carrot")
print(s.is_empty())
print(s)
