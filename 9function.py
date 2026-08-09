
# 1. Function to return maximum number among 3 numbers
def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c:
        return b
    else:
        return c

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

ans = maximum(a, b, c)
print("Maximum number is:", ans)

# 2. Function to return square of a number
def square(n):
    return n * n

n = int(input("Enter a number: "))

ans = square(n)

print("Square =", ans)

#3.Function to return cube of a number
def cube(n):
    return n * n * n

n = int(input("Enter a number: "))

ans = cube(n)

print("Cube =", ans)

#4.Function to return sum of numbers between ranges using while loop
def range_sum(start, end):
    total = 0

    while start <= end:
        total = total + start
        start = start + 1

    return total


start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

ans = range_sum(start, end)

print("Sum =", ans)

#5.Function to return average of marks of 5 subjects using while loop
def average_marks():
    total = 0
    count = 1

    while count <= 5:
        marks = float(input("Enter marks: "))
        total = total + marks
        count = count + 1

    average = total / 5
    return average


ans = average_marks()

print("Average marks =", ans)


#6.Function to return product of numbers from 1 to n using while loop
def product(n):
    result = 1
    i = 1

    while i <= n:
        result = result * i
        i = i + 1

    return result


n = int(input("Enter n: "))

ans = product(n)

print("Product =", ans)

#7.Function to return factorial using while loop
def factorial(n):
    fact = 1
    i = 1

    while i <= n:
        fact = fact * i
        i = i + 1

    return fact


n = int(input("Enter a number: "))

ans = factorial(n)

print("Factorial of", n, "is", ans)

#8.Function to check whether a number is prime using while loop
def prime(n):
    i = 2

    while i < n:
        if n % i == 0:
            return False
        i = i + 1

    return True


n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime Number")
elif prime(n):
    print("Prime Number")
else:
    print("Not a Prime Number")

#9.Function to check whether a number is composite using while loop
def composite(n):
    i = 2

    while i < n:
        if n % i == 0:
            return True
        i = i + 1

    return False


n = int(input("Enter a number: "))

if n <= 1:
    print("Neither Prime nor Composite")
elif composite(n):
    print("Composite Number")
else:
    print("Not a Composite Number")

#10.Function to check whether a number is a perfect number using while loop

def perfect(n):
    i = 1
    total = 0

    while i < n:
        if n % i == 0:
            total = total + i
        i = i + 1

    if total == n:
        return True
    else:
        return False


n = int(input("Enter a number: "))

if n <= 0:
    print("Not a Perfect Number")
elif perfect(n):
    print("Perfect Number")
else:
    print("Not a Perfect Number")





