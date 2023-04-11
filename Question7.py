# question 7
import math
def calculate_gcd(intx, inty):
    x = 0
    y = 0
    greatestcommondemoninator = 0
    #determine which number is higher
    if intx > inty:
        x = intx
        y = inty
    else:
        y = intx
        x = inty
    for n in range (2,x+1):
        if y % n == 0 and x % n == 0 and n > greatestcommondemoninator:
            print(n)
            greatestcommondemoninator = n
    return greatestcommondemoninator




user_input_x = int(input("Enter a nonneagtive integer: "))
user_input_y = int(input("Enter a nonneagtive integer: "))
if user_input_y >0 and user_input_x >0:
    print(calculate_gcd(user_input_x,user_input_y))