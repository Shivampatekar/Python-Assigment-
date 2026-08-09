#1.Area of Square
length = float(input("Enter length: "))

area = lambda l: l * l

print("Area of square =", area(length))

#2. Cube of a Number
num = int(input("Enter a number: "))

cube = lambda n: n ** 3

print("Cube =", cube(num))


#3.Maximum of Two Numbers
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

maximum = lambda a, b: a if a > b else b

print("Maximum =", maximum(num1, num2))


#4.Area of Rectangle
length = float(input("Enter length: "))
width = float(input("Enter width: "))

area = lambda l, w: l * w

print("Area of rectangle =", area(length, width))

#5.Celsius to Fahrenheit

#Formula: F = (C × 9/5) + 32

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = lambda c: (c * 9/5) + 32

print("Temperature in Fahrenheit =", fahrenheit(celsius))

#6.Fahrenheit to Celsius
#Formula: C = (F - 32) × 5/9

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = lambda f: (f - 32) * 5/9

print("Temperature in Celsius =", celsius(fahrenheit))

#7.Last Digit of a Number
num = int(input("Enter a number: "))

last_digit = lambda n: abs(n) % 10

print("Last digit =", last_digit(num))

#8.Perimeter of Square
#Formula: Perimeter = 4 × length

length = float(input("Enter length: "))

perimeter = lambda l: 4 * l

print("Perimeter of square =", perimeter(length))

#9.Check Whether String Contains 'a'
string = input("Enter a string: ")

check = lambda s: 'a' in s

print("Contains 'a':", check(string))

#10.Check Leap Year

year = int(input("Enter year: "))

leap_year = lambda y: "Leap Year" if (y % 400 == 0 or (y % 4 == 0 and y % 100 != 0)) else "Not a Leap Year"

print(leap_year(year))





