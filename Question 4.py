#question four


def calculate_factorial(factorial_int):
    # if factorial int = 5, then 1x2x3x4x5
    running_total = 1
    for n in range(1, factorial_int+1):
        running_total = n * running_total
        #print(running_total)
        #print(n)
    return running_total
user_input = int(input('please enter positive non negative number: '))

print('factor of this number is:', calculate_factorial(user_input))