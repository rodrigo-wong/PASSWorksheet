'''
The Modulo operator allows us to return the remainder of an equation. Consider the 
following: 

    4 % 2 = 0 
    This equation says that 2 goes into 4 twice, therefore the remainder is 0 

    Let's try one more: 

    10 % 3 = ___
    How many times does 3 go into 10? 3 Times, right?
    3 + 3 + 3 = 9 
    So now we see that 3 can't go into 10 anymore than that, so
    this means that the remainder is 1. 
    10 % 3 = 1

FizzBuzz:
Design a module/function named fizzBuzz that has one integer parameter, num. 
In your code, loop through values that go from 1 all the way to the number
that the user entered (num). 

- Whenever a number is perfectly divisible by 3, output the word "Fizz" along 
with the number. 
- Whenever a number is perfectly divisible by 5, output the word "Buzz" along
with the number. 
- Wheneve ra number is perfectly divisible by 3 AND by 5, output the word 
"FizzBuzz". 

Note: Do not start your for loop from 0. 
Note: Do not use an "else" in your if block, try to code the condition specifically!
'''

def fizzBuzz( num ):
    for current_number in range(1, num):
        if current_number % 3 == 0 and current_number % 5 == 0:
            print("FizzBuzz", current_number)
        elif current_number % 3 == 0:
            print("Fizz", current_number)
        elif current_number % 5 == 0:
            print("Buzz", current_number)

fizzBuzz( 20 )