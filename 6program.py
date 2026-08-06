#1.WAP to check if numbers are divisible by 4 and 5

num1 = int(input("Enter number: "))

if num1 % 4 == 0 and num1 % 5 == 0:
    print(num1, "is divisible by 4 and 5")
else:
    print(num1, "is not divisible by 4 and 5")

#2.WAP to determine whether the entered angles define a right-angled triangle. T ake three values of angle from the user.

angle1 = int(input("Enter angle 1: "))
angle2 = int(input("Enter angle 2: "))
angle3 = int(input("Enter angle 3: "))

if angle1 + angle2 + angle3 == 180 and (angle1 == 90 or angle2 == 90 or angle3 == 90):
    print("It is a right-angle triangle")
else:
    print("It is not a right-angle triangle")

#3.take two numbers from the users and print the sum of those numbers If the sum is even.

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sumData = num1 + num2

if sumData % 2 == 0:
    print(sumData, "is Even")


#4. Take a number from the user and check whether it is present in the list

list1 = [10, 20, 30, 40, 50]

num = int(input("Enter number: "))

if num in list1:
    print("Available")


#5.Print "Core2web" number of times entered by user if the number is even
num = int(input("Enter number: "))

if num % 2 == 0:
    for i in range(num):
        print("Core2web")

#6.Check if a given number is odd using if

num = int(input("Enter number: "))

if num % 2 != 0:
    print("Odd")

#7.Take two numbers, check if both are odd, and then print their sum

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 % 2 != 0 and num2 % 2 != 0:
    print(num1 + num2)

#8.Take a single character and check if its ASCII value is even

char1 = input("Enter a character: ")

if ord(char1) % 2 == 0:
    print(char1)
else:
    print("odd")


#9.Take two characters and check if ASCII values of both characters are odd

char1 = input("Enter first character: ")
char2 = input("Enter second character: ")

ascii1 = ord(char1)
ascii2 = ord(char2)

if ascii1 % 2 != 0 and ascii2 % 2 != 0:
    print(ascii1 + ascii2)
else:
    print("sum is odd")


#10.Take the number from the user and modulus with 8 if the remainder of the number is 3, then print the number; otherwise, print the remainder.

num = int(input("Enter number: "))

remainder = num % 8

if remainder == 3:
    print(num)
else:
    print(remainder)




