n = int(input())

for i in range(n):
    space = n - i - 1
    stars = i + 1
    print(space * " ", stars * "* ")

for i in range(n - 2, -1, -1):
    space = n - i - 1
    stars = i + 1
    print(space * " ", stars * "* ")

