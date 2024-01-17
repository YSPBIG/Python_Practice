#Guess Number

import random

#Generate a random mystery number
mystery_number = random.randint(1,10)

#User guess the number of mystery number
guess_number = int(input("Guess the mystery number as whole number between 1 and 10"))

#Check if the number is correct or not?
if guess_number == mystery_number:
    print("Your guess is Correct!")
else:
    print("Your guess is wrong")
    print("The mystery_number is :", mystery_number)

    