#2

r = float(input("Podaj srednice kola: "))
pole = 3.14 * (r*r)
obwod = (2 * 3.14) * r
print(f'obwod = {obwod}, pole = {pole}')

#3 

temp = float(input("podaj temperature w stopniach celsjusza: "))
kelvin = temp + 273.15
fahrenheit = 2 * (temp - (0,1 * temp)) + 32
print(f'Temperatura w k: {kelvin}, temperatura w F: {fahrenheit}')

#4

wzrost = float(input("Podaj wzrost w cm: "))
stopy = wzrost/30.48
cale = wzrost/2.54
print(f"Twój wzrost w stopach{stopy}, w calach: {cale}")

#5

swift = input('Podaj kod SWIFT: ')
print(f'Bank Code: {swift[0:3]}')
print(f'Country Code: {swift[4:5]}')
print(f'Localization Code: {swift[6:7]}')
if len(swift) > 8:
    print(f'Kod oddzialu: {swift[8:10]}')

#6

distance = int(input('Enter distance in km: '))
fuel_price = float(input('Enter fuel price per liter: '))
fuel_consumption = float(input("Enter fuel consumption: "))
total_fuel_consumption = (fuel_consumption/100) * distance
total_cost = total_fuel_consumption * fuel_price
print(f'Total fuel consumption: {total_fuel_consumption}')
print(f'Total cost: {total_cost}')

#7

number = int(input("Podaj liczbe w systemie dziesietnym: "))
dwojkowy = bin(number)
szestnastkowy = hex(number)
print(f'Dwojkowy: {dwojkowy}, szestnastkowy: {szestnastkowy}')