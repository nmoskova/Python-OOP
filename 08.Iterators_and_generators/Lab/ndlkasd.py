my_list = [1, 3, 6, 10]

a = (x**2 for x in my_list)
for _ in a:
    print(_)
