#!/usr/bin/python

yn = input("Continue? Yes or No: ")
yn = yn.lower()

if yn[0] =='y':
    print("You chose 'Yes.'")
elif yn[0] =='n':
    print("You chose 'No.'")
elif yn =='spam':
    print("You found an easter egg.")
else:
    print("You entered an invalid response.")
