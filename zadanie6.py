'''
# A program that calculates the number of characters
# of your name, surname and full name
#
name = input('Name: ') 
surname = input('Surname: ')
characters_in_name = len(name)
print(f'Your name has {characters_in_name} characters')
print(f'Your surname has {len(surname)} characters')
print(f'Your full name has {len(name + surname)} characters') 

####

# A program that prints your initials
#
name = input('Name: ')
surname = input('Surname: ')
print(name[0])
print(surname[0])

####

# A program that prints a university abbreviation
#   
university = "Krakow University of Economics"
print(university)
print(university[0] + university[7] + university[-9])

####

# A program for printing detailed information.
#
employee = "Mr. John May, born on 1998-02-16"
print(f'Name: {employee[4:8]}')
print(f'Surname: {employee[9:12]}')
print(f'Born: {employee[-10:]}')
print(f'Initials: {employee[4]} {employee[9]}')

####

# a program that prints a 9-digit telephone number
# entered from the keyboard as three groups of 3 digits each,
# separated by a dash character.
#
phone = input('Enter phone number: ')
print(f'{phone[:3]}-{phone[3:6]}-{phone[-3:]}')

####

# A program to print numerical representations of characters.
#
print(f'a {ord('a')}')
print(f'b {ord('b')}')
print(f'z {ord('z')}')
print(f'A {ord('A')}')
print(f'B {ord('B')}')
print(f'Z {ord('Z')}')
print(f'= {ord('=')}')
print(f'+ {ord('+')}')
print(f'€ {ord('€')}')'''

####

###
# A program that prints a numerical representation of each letter of your name.
#
x = int(0)
name = input('Name: ') # replace John with your name
for i in name:
    print(f'The letter {name[x]} has a code {ord(name[x])}')
    x = x+1

####

# A program that calculates
# how many letters are between two given letters
#
first = input('Enter first letter: ')
last = input('Enter last letter: ')
first_letter_code = ord(first)
last_letter_code = ord(last)
number_of_letters = last_letter_code - first_letter_code
print(f'Between {first} and {last} is {number_of_letters - 1} letters')

####

# Character code conversion
#
print(chr(67),chr(111),chr(111),chr(108),chr(33))

####

###
# String manipulation
#

movie = "The Lord of the Rings: The Return of the King"

# print number of characters
print('Number of characters: ', len(movie))

# print title in capital letters
print(movie.upper())

# print title in small letters
print(movie.casefold())

# print how many times the vowel "e" appears in the title
print(movie.count('e'))

# print where in the text is the word "Lord"
print(movie.find("Lord"))

# print where in the text is the word "dragon"
print(movie.find('d'))
print(movie.find('r'))
print(movie.find('a'))
print(movie.find('g'))
print(movie.find('o'))
print(movie.find('n'))