def get_primes(list_of_integers):
    positive_numbers = [num for num in list_of_integers if num > 1]
    for num in positive_numbers:
        prime_number = False
        step = 1
        while True:
            if num - step == 1:
                prime_number = True
                break

            divisor = num - step
            if num % divisor == 0:
                break

            step += 1

        if prime_number:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

print(list(get_primes([-2, 0, 0, 1, 1, 0])))