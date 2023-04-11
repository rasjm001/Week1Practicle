# Question 5

def number_triangle(int):
    string = str('')
    for n in range(1, int+1):
        string = string + str(n)
        print(string)

user_input = int(input('enter number between one and 9: '))
if user_input >= 1 and user_input <= 9:
    print('correct input')
    number_triangle(user_input)
else:
    print('incorrect input')