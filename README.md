Week one practicle:
The following exercises allow you to practise the Python concepts you have learnt so far by putting them all together to solve problems:

Write a basic Python function called distance(). This function should take two parameters: velocity and time. The operations performed by this function should be consistent with the formula below:

distance = velocity * time
The function should return the distance travelled in metres at the given velocity (in metres per second) for the given amount of time (in seconds).

In physics, a physical body that is in motion is said to have kinetic energy. The following formula can be used to determine a moving physical body's kinetic energy:

KE=12mv2

where KE is the kinetic energy, m is the body's mass in kilograms, and v is the body's velocity in metres per second.

Write a function named kinetic_energy() that accepts a body's mass (in kilograms) and velocity (in metres per second) as arguments. The function should return the amount of kinetic energy that the physical body has.

Write a program that asks the user to enter values for mass and velocity, then calls the kinetic_energy() function to get the body's kinetic energy. Finally, the program displays the computed kinetic energy to the screen.

A prime number is a number that is only evenly divisible by itself and 1. For example, the number 5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is not prime because it can be evenly divided by 1, 2, 3, and 6.

Write a Boolean function named is_prime() which takes an integer as an argument and returns true if the argument is a prime number, or false otherwise.

Write a program that prompts the user to enter an integer number and displays all of the prime numbers from 1 to that number. The program should have a loop that calls the is_prime() function.

In mathematics, the notation n! represents the factorial of the number n!. The factorial of a nonnegative number can be defined by the following rules:

if n = 0 then n! = 1
if n > 0 then n! = 1 x 2 x 3 x ... x n
Write a function called calculate_factorial() which takes a number as an argument and returns the factorial of that number.

Write a program that prompts the user to enter an integer number and displays the value of the factorial of that number.

Enter a nonnegative integer: 4 [ENTER]
The factorial of 4 is 24
Write a function named number_triangle() which takes an integer between 1 and 9 as an argument and displays a number triangle with the numbers from 1 to that number. For example, if the argument number is 5, then the number triangle would be:

1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
Write a function named reverse_number_triangle() which takes an integer between 1 and 9 as an argument and displays a reverse number triangle with the numbers from 1 to that number. For example, if the argument number is 5, then the number triangle would be:

1 1 1 1 1
  2 2 2 2
    3 3 3 
      4 4
        5
The greater common divisor GCD of two positive integers x and y is determined as follows:

if x can be divided by y then GCD(x, y) = y
Otherwise, GCD(x, y) = GCD(y, reminder of x/y)
Write a function called calculate_gcd() which takes two positive integers as arguments and returns the GCD of those two integers.

Write a program that prompts the user to enter two integer numbers and displays the value of their GCD.

Enter a nonneagtive integer: 49 [ENTER]
Enter a nonneagtive integer: 28 [ENTER]
The greatest common divisor of 49 and 28 is 7
A palindrome is a word, number, phrase, or other sequences of characters that reads the same backward as forward, such as madam, racecar.

Write a Boolean function named is_palindrome() which takes a string as an argument and returns true if the argument is a palindrome, or false otherwise.

Sentence-length palindromes ignore capitalisation, punctuation, and word boundaries, they only consider letters or digits.

Write a program that reads a file named palindrome_input.txt, then tests each line of the file to check if it is palindrome or not, and finally writes each line and whether it is palindrome or not on a line in another file named palindrome_output.txt. The program should have a loop that calls the is_palindrome() function.

The palindrome_input.txt file looks like:

redivider 
I am Iron Man
civic
11000011
12345808054321
Never odd or even
02-02-2020
kayak
A man, a plan, a canal - Panama
10001000
Madam, I'm Adam
The palindrome_output.txt file will be as follows:

redivider = Palindrome
I am Iron Man = Not Palindrome
civic = Palindrome
11000011 = Palindrome
12345808054321 = Not Palindrome
Never odd or even = Palindrome
02-02-2020 = Palindrome
kayak = Palindrome
A man, a plan, a canal - Panama = Palindrome
10001000 = Not Palindrome
Madam, I'm Adam = Palindrome
An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For this problem, we will consider alphabetical letters (i.e. A .. Z, a .. z) and numerical digits (0 .. 9) as the letters of the word or phrase.

Write a Boolean function named is_anagram() which takes a string as an argument and returns true if the argument is an anagram, or false otherwise.

Write a program that reads a file named anagram_input.txt, then tests every two lines of the file to check if the strings of those two lines are anagram to one another or not, and finally writes the two lines and whether they are anagram or not on a line in another file named anagram_output.txt. The program should have a loop that calls the is_anagram() function.

The anagram_input.txt file looks like:

Binary
Brainy
1234500
5004231
Computer
Computer
1100
1010
Adobe
Abode
Python
Throne
Listen
Silent
Eleven plus two
Twelve plus one
Brother
Sister
Father
Mother
11110
10111111
Madam Curie 
Radium came
The anagram_output.txt file will be as follows:

Binary : Brainy = True
1234500 : 5004231 = True
Computer : Computer = False
1100 : 1010 = True
Adobe : Abode = True
Python : Throne = False
Listen : Silent = True
Eleven plus two : Twelve plus one = True
Brother : Sister = False  
Father : Mother = False
11110 : 10111111 = False
Madam Curie : Radium came : True
Write a program that outputs the lyrics for "Ninety-nine Bottles of Beer on the Wall." Your program should print the number of the bottles in English not as a number.

Your output should be something like this:

Ninety-Nine bottles of beer on the wall
Ninety-Nine bottles of beer!
Take one down, pass it around,
Ninety-Eight bottles of beer on the wall.

…

One bottle of beer on the wall 
One bottle of beer!
Take one down, pass it around, 
No more bottles of beer on the wall.

No more bottles of beer on the wall 
No more bottles of beer! 
Go to the store and buy some more, 
Ninety-Nine bottles of beer on the wall.
Your program must not just have ninety-nine output statements.

Consider how you can decompose the problem.

Hint: Get the program working with numbers first, then work on converting to words.

