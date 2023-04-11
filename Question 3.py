#Question 3

def is_prime(integer_to_check):
    boolean_prime = True

    for number in range(2,integer_to_check):
        if integer_to_check % number == 0:
           # print("is not prime")
            boolean_prime = False

    return boolean_prime


user_input = int(input('please input a positive whole number to check: '))
for n in range(2, user_input):
    if is_prime(n)== True:
        print(n)

print(is_prime(user_input))
