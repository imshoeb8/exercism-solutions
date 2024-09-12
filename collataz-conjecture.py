def steps(number):
    if number <= 0: raise ValueError("Only positive integers are allowed")
    if number == 1: return 0
    number = number / 2 if number % 2 == 0 else number * 3 + 1
    return 1 + steps(number)

def steps(n):
    if n < 1:
        raise ValueError('Only positive integers are allowed')

    steps = 0

    while n > 1 :
        n = 3 * n + 1 if n % 2 else n / 2
        steps += 1


    return steps
    