# 1. Function to print the table of a number
def table(n):
    print(n, "* 1 =", n * 1)
    print(n, "* 2 =", n * 2)
    print(n, "* 3 =", n * 3)
    print(n, "* 4 =", n * 4)
    print(n, "* 5 =", n * 5)
    print(n, "* 6 =", n * 6)
    print(n, "* 7 =", n * 7)
    print(n, "* 8 =", n * 8)
    print(n, "* 9 =", n * 9)
    print(n, "* 10 =", n * 10)

num = int(input("Enter a number: "))
table(num)

# 2.Function to check Even or Odd
def check_even_odd(n):
    if n % 2 == 0:
        print("Even")
    else:
        print("Odd")

num = int(input("Enter a number: "))
check_even_odd(num)

#3.Function to check voting eligibility
def voting(age):
    if age >= 18:
        print("Eligible for voting")
    else:
        print("Not eligible for voting")

age = int(input("Enter your age: "))
voting(age)

#4.Arithmetic operations using function
def arithmetic(a, b):
    print("Addition =", a + b)
    print("Subtraction =", a - b)
    print("Multiplication =", a * b)
    print("Division =", a / b)
    print("Modulus =", a % b)
    print("Floor Division =", a // b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

arithmetic(num1, num2)

#5. Function to check Vowel or Consonant
def check_vowel(ch):
    if ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u':
        print("Vowel")
    else:
        print("Consonant")

ch = input("Enter a character: ")
check_vowel(ch)

#6.Function to print ASCII value
def ascii_value(ch):
    print("ASCII value =", ord(ch))

ch = input("Enter a character: ")
ascii_value(ch)

#7.Function to find maximum between two numbers
def maximum(a, b):
    if a > b:
        print("Maximum =", a)
    else:
        print("Maximum =", b)

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

maximum(num1, num2)

#8.Function using Keyword Arguments

#Student details: Name, Age and Course

def student_details(name, age, course):
    print("Name =", name)
    print("Age =", age)
    print("Course =", course)

student_details(
    name="Shivam",
    age=20,
    course="AI & Data Science"
)

#9.Variable-Length Arguments *args se Average

def average(*args):
    total = sum(args)
    avg = total / len(args)
    return avg

ans = average(10, 20, 30, 40, 50)
print("Average =", ans)

#10.Variable-Length Arguments *args se Average

def outer():
    return "Hello, I'm the inner function!"

ans = outer()
print(ans)

# 11. Function to Return Area of Circle

def circle_area(radius):
    area = 3.14 * radius * radius
    return area

radius = float(input("Enter radius: "))

area = circle_area(radius)

print("Radius =", radius)
print("Area =", area)







