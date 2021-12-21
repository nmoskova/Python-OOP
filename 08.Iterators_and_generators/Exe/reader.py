def read_next(*args):
    for arg in args:
        if isinstance(arg, dict) or isinstance(arg, set):
            for key in arg:
                yield key.lower()
        else:
            idx = 0
            while idx < len(arg):
                yield arg[idx]
                idx += 1


for item in read_next("string", (2,), {"d": 1, "I": 2, "c": 3, "t": 4}):
    print(item, end='')

for i in read_next("Need", (2, 3), ["words", "."]):
    print(i)
