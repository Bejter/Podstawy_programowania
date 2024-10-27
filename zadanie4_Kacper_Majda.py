#1.
company = "ABC Data"
phone = "555-123-009"
employees = 25
remote_work = True
big_company = employees > 100
income = 4500000
income_per_person = income / employees

print("company, " + str(type(company)) + ", " + str(company))
print("phone, " + str(type(phone)) + ", " + str(phone))
print("employees, " + str(type(employees)) + ", " + str(employees))
print("remote_work, " + str(type(remote_work)) + ", " + str(remote_work))
print("big_company, " + str(type(big_company)) + ", " + str(big_company))
print("income, " + str(type(income)) + ", " + str(income))
print("income_per_person, " + str(type(income_per_person)) + ", " + str(income_per_person))

#2.
number1 = 71
number2 = 14
number3 = 25
result = number1 + number2 + number3
print('Number 1: ', number1)
print('Number 2: ', number2)
print('Number 3: ', number3)
print('The result of summation: ', result)

#3.

x = 7
y = 34
z = 0 
print("Before swapping: x=", x, "y=", y)

z = x
x = y
y = z

print("After swapping: x=", x, "y=", y)

#4.
speed_kmh = 70
speed_ms = speed_kmh * 1000 / 3600
print(speed_kmh, "km/h = ", speed_ms, "m/s")

#5.

import math
a = 5
b = 8
diagonal = math.sqrt(a**2 + b**2)
print(diagonal)

#6.

height = float(input("Podaj wzrost w metrach: "))
d = 3.57 * math.sqrt(height)
print(d)

#7.
total = 8000000000
north = 7200000000
south = total - north
print("World population: ", total)
print("Northern Hemisphere: ", north)
print("Northern Hemisphere in %: ", north/total*100)
print("Southern Hemisphere: ", south)
print("Southern Hemisphere in %: ", south/total*100)

#8.

mat = 5
art = 4
music = 5
history = 3
average = (mat + art + music + history)/4
print("Average grade is", average)