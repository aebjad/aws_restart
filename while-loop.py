####  Working with a while loop
### A while loop makes a section of code repeat until a certain condition is met.
### In this exercise, you will create a Python script that asks the user to correctly guess a number.

import random


print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

# Importing random and writing a while loop
# You will use the import command to include code that someone else wrote.
# Up to now, you have been using built-in functions. Recall that a function is a piece of reusable code.
number = random.randint(1,10)
isGuessRight = False
while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))
        
        