def number_increment(numbers):

    def increase():

        nums = [num + 1 for num in numbers]
        return nums

    return increase()


print(number_increment([1, 2, 3]))