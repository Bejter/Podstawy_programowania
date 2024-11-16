# A program that reads your first and last name from the keyboard.
# Store this data in two separate variables.
# Then, print your full name i.e. first and last name separated by a single space.
first_name = input('Enter your first name: ')
last_name = input('Enter your last name: ')
full_name = first_name + ' ' + last_name
print(f'Your first name is {first_name} and your last name is {last_name}')
print(f'And your full name is {full_name}')

####

###
# A program to calculate the volume and surface area of ​​a cube.
# 
cube_side_string = input('Enter cube side: ')
cube_side = int(cube_side_string)
cube_volume = cube_side * cube_side * cube_side
cube_surface_area = cube_side * cube_side * 6
print(f'The volume of a cube with side {cube_side} is {cube_volume}')
print(f'The surface area of a cube with side {cube_side} is {cube_surface_area}')

####

###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))

volume = a * b * c
surface_area = a * b * 6

print(f'Volume of cuboid is {volume}')
print(f'Surface area of cuboid is {surface_area}')

####

amount = float(input('Amount: '))
vat_amount = 23/100 * amount
round(vat_amount, 2)
round(amount, 2)
print(f'Amount = {amount}')
print(f'VAT 23% = {vat_amount}')

####

price = float(input('price: '))
discount = int(input('discount in %: '))
discount_value = discount/100
discounted_price = price - discount_value * price
reduction = price - discounted_price
print(f'Price: {price}')
print(f'Discount: {discount}')
print(f'Discounted price: {discounted_price}')
print(f'Reduction: {reduction}')