# Number guess by User 

import random

def user_guess(number):
    random_number = random.randint(1, number)
    guess = 0
    guess_count = 0
    while guess != random_number:
        guess = int(input(f'Guess the number between 1 and {number}: '))
        guess_count += 1
        if guess > random_number:
            print('Sorry, guess again, Too High')
        elif guess < random_number:
            print('Sorry, guess again. Too Low')
    print(f'Great Job! You guess {random_number} number in {guess_count} guesses. ')


print('Selecting a range of number from 1 to ....')
number = int(input('Enter a last number: '))
user_guess(number)    