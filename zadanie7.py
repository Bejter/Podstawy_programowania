#1

age = int(input('Enter age: '))
no_tax = age < 27
print(f'Exemption from paying taxes: {no_tax}')

#2

password = input('Enter password: ')
password_ok = len(password) >= 8
print(f'Password length is valid: {password_ok}')

#3

number = int(input('Enter number: '))
even = number%2 == 0
print(f'Number is even: {even}')

#4

number = int(input('Enter number: '))
can_cut = number/3.14 >= 50
print(f'Cam cut tree: {can_cut}')

#5

car_number = input('Enter car registration number')
is_krakow = car_number[0:2] == "KR" or "KK"
print(f'Car is from Krakow: {is_krakow}')

#6

speed_user = int(input('Enter number: '))
is_overspeeding = speed_user < 40 and speed_user > 140
print(f'Car is not in the limit: {is_overspeeding}')

#7
import random
random_number = random.randint(5,10)
print(random_number)

#8

dice_roll_1 = random.randint(1,6)
dice_roll_2 = random.randint(1,6)
dice_roll_3 = random.randint(1,6)
total = dice_roll_1 + dice_roll_2 + dice_roll_3
print(f"Total: {total}")

#9

dice_roll = random.randint(1,6)
is_1_or_6 = dice_roll == 1 or dice_roll == 6
print(f"Special number (1 or 6): {is_1_or_6}" )

#10

# COMPUTER TURN
computer = random.randint(1,6)
# YOUR TURN
you = input("guess the number from 1 to 6")
is_guessed = you == computer
print(f'You won: {is_guessed}')