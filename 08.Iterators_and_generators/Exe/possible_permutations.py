from itertools import permutations


def possible_permutations(some_list):
    for permutation in permutations(some_list):
        yield list(permutation)


[print(n) for n in possible_permutations([1, 2, 3])]