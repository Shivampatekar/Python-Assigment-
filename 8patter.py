#1. Take rows from user
rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(rows):
        print("*", end="  ")
    print()

#2.Print Odd Numbers Pattern

rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = 1
    for j in range(rows):
        print(num, end="  ")
        num = num + 2
    print()

#3.Increasing Odd Pattern
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    num = i
    for j in range(rows):
        print(num, end="  ")
        num = num + 2
    print()
# or 

rows = int(input("Enter number of rows: "))

for i in range(rows):
    num = (i * rows) + 1

    for j in range(rows):
        print(num, end="  ")
        num = num + 2

    print()

#4.Star patter

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(i):
        print("*", end="  ")
    print()

#5.Number Triangle

rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()

# 6.Reverse Number Triangle
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(rows, rows - i, -1):
        print(j, end="  ")
    print()

#7.Reverse Star Pattern
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print("*", end="  ")
    print()

#8.Reverse Number Pattern
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()

#9.Number Pattern
rows = int(input("Enter number of rows: "))

for i in range(rows, 0, -1):
    for j in range(i):
        print(i, end="  ")
    print()

#10.Number Triangle
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end="  ")
    print()

#11.Reverse Number Triangle
rows = int(input("Enter number of rows: "))

for i in range(1, rows + 1):
    for j in range(rows, rows - i, -1):
        print(j, end="  ")
    print()
    












