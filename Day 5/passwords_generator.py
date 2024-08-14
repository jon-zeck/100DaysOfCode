''' Day 5: Password Generator. Generate a password_list of 16 characters. '''
import random

lower_letters = "abcdefghijklmnopqrstuvwxyz"
upper_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
symbols = "~`!@#$%^&*()_-+={[}]|\\:;\"'<,>.?/"
numbers = "0123456789"

password_list = []

password_list += random.choice(lower_letters)
password_list += random.choice(upper_letters)
password_list += random.choice(symbols)
password_list += random.choice(numbers)

for i in range(12):
    probability = random.randint(1, 100)
    match probability:
        case probability if probability <= 25:
            password_list += random.choice(lower_letters)
        case probability if probability > 25 and probability <= 50:
            password_list += random.choice(upper_letters)
        case probability if probability > 50 and probability <= 75:
            password_list += random.choice(symbols)
        case probability if probability > 75:
            password_list += random.choice(numbers)

random.shuffle(password_list)

password = ''.join(password_list)
print(password)
input()

''' I did not know about random.choice and random.shuffle! Very useful. '''
