# question 6

def reverse_number_triangle(interger):
    height_value= interger+1
    spacevalue = 0
    blankstr = str(' ')
    for n in range(1, height_value):
        spacevalue = n-1
        print(blankstr * spacevalue, str(n)*(height_value-n))
       # print (str(n) * (height_value-n))


user_input = int(input("please enter number between one and 9: "))
if user_input >=1 and user_input <=9:
    print('correct input')
    reverse_number_triangle(user_input)
else:
    print('incorrect input, bye')