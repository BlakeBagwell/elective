def count_down(number):
    if(number == 0):
        return None
    print(number)
    count_down(number - 1)


def factorial(number):
    if number == 1:
        return number
    else:
        return number * factorial(number - 1)


print (factorial(3))
