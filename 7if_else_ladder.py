'''#Assignment
Instructions:
Write a Python program for each of the following questions using only if–else
ladder statements.
*Note: Do not use loops, match-case, or functions.'''

#1. Blood Donation Eligibility

age = int(input("Enter age: "))
weight = float(input("Enter weight: "))
hb = float(input("Enter hb: "))

if age >= 18 and age <= 65 and weight > 50 and hb > 12.5:
    print("Eligible for blood donation")
else:
    print("Not eligible for blood donation")

#2. Student Grade Evaluator
marks = int(input("Enter marks: "))

if marks >= 90 and marks <= 100:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
elif marks >= 60:
    print("Grade: C")
elif marks >= 50:
    print("Grade: D")
else:
    print("Grade: Fail")

#3. Electricity Bill Calculator
units = float(input("Enter units: "))

if units <= 100:
    bill = units * 5
elif units <= 200:
    bill = units * 7
elif units <= 300:
    bill = units * 10
else:
    bill = units * 15

print("Total Bill: ₹", bill)

# 4. Income Tax Calculator
income = float(input("Enter income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print("Tax to be paid: ₹", tax)

#Q5. Temperature Condition

temperature = float(input("Enter temperature: "))

if temperature < 0:
    print("Freezing Cold")
elif temperature <= 10:
    print("Very Cold")
elif temperature <= 20:
    print("Cold")
elif temperature <= 30:
    print("Warm")
elif temperature <= 40:
    print("Hot")
else:
    print("Extreme Heat")


#6.Character Classifier
char = input("Enter character: ")

if char >= 'A' and char <= 'Z':
    print("Uppercase Letter")
elif char >= 'a' and char <= 'z':
    print("Lowercase Letter")
elif char >= '0' and char <= '9':
    print("Digit")
else:
    print("Special Character")

#7. University Admission System
percentage = float(input("Enter percentage: "))
score = float(input("Enter exam score: "))

if percentage >= 90 and score >= 90:
    print("Admission in Elite Program")
elif percentage >= 80 and score >= 70:
    print("Admission in Standard Program")
elif percentage >= 60 and score >= 50:
    print("Admission in Basic Program")
else:
    print("Not eligible")

#8.Number Category Analyzer
number = int(input("Enter number: "))

if number == 0:
    print("Zero")
elif number > 0 and number % 2 == 0:
    print("Positive Even")
elif number > 0 and number % 2 != 0:
    print("Positive Odd")
elif number < 0 and number % 2 == 0:
    print("Negative Even")
else:
    print("Negative Odd")

#9.Shopping Discount System
amount = float(input("Enter purchase amount: "))

if amount < 1000:
    discount = 0
    discount_percent = 0
elif amount < 5000:
    discount = amount * 0.05
    discount_percent = 5
elif amount < 10000:
    discount = amount * 0.10
    discount_percent = 10
elif amount < 20000:
    discount = amount * 0.20
    discount_percent = 20
else:
    discount = amount * 0.30
    discount_percent = 30

final_amount = amount - discount

print("Discount Applied:", discount_percent, "%")
print("Final Amount: ₹", final_amount)


# 10.Triangle Type Checker

angle1 = float(input("Enter first angle: "))
angle2 = float(input("Enter second angle: "))
angle3 = float(input("Enter third angle: "))

total = angle1 + angle2 + angle3

if total != 180:
    print("Invalid Triangle")
elif angle1 < 90 and angle2 < 90 and angle3 < 90:
    print("Triangle is Acute")
elif angle1 > 90 or angle2 > 90 or angle3 > 90:
    print("Triangle is Obtuse")
else:
    print("Triangle is Right Angled")














