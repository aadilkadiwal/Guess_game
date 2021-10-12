# Number guess by Computer 

import random

def computer_guess(high_num):
    count_guess = 0
    low_num = 1
    user_reply = ''
    while 'c' != user_reply:
        comp_guess = int((low_num + high_num)/2)
        count_guess += 1
        print(f'I guess {comp_guess}.')
        user_reply = input("Enter 'c' if Correct, Enter 'l' if Low, Enter 'h' if High : ")
        if 'l' == user_reply.lower():
            low_num = comp_guess
            print('Lower')
        elif 'h' == user_reply.lower():
            high_num = comp_guess
            print('Higher')        
    print(f'Yeah! I guess {comp_guess} number in {count_guess} guesses.')

print('Tell me the range of number from 1 to ....')
high_num = int(input('Enter a last number : ' ))
print(f'Select a Random number from 1 to {high_num}.')
print('I will guess that number.')

computer_guess(high_num)