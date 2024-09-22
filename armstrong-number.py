def is_armstrong_number(number):
    base = list(str(number))
    exponent = len(base)
    summation = 0
    for index in base:
         summation += int(index)**exponent
    return summation == number
