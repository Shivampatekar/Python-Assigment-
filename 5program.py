


#1.find the maaximu between 2 number 

x=int(input("enter number1:"))
y=int(input("enter number2:"))

if x>y:
    print("x is max")
else:
    print("x small")

#2. check number is positive ,negative or zero
num=-2

if num>0:
    print("positive")
elif num<0:
    print("Negative")
else:
    print("zero")

#3. find number is even or odd 
num = 4

if num % 2 == 0:
    print("even")
else:
    print("odd")

#4. check number is divisible by 5 or not 

num = 3

if num % 5 ==0:
    print("number is divisible by 5")
else:
    print("not divisible by 5")



#5. take inter rangig for 0 to 6 and print corrosponding week 

day=int(input("enter dat o to 6: "))

if day==0:
    print("monday")
elif day==1:
    print("thusday")
elif day==2:
    print("Wednesday")
elif day==3:
    print("Thursday")
elif day==4:
    print("Friyday")
elif day==5:
    print("saturday")
else:
    print("sunday")

# 6.Write a Program to check whether the Character is an Alphabet or not.

ch = input("Enter a character: ")

if len(ch) == 1:
    if ('a' <= ch <= 'z') or ('A' <= ch <= 'Z'):
        print(" is an alphabet.")
    else:
        print("is not an alphabet.")
else:
    print("Please enter exactly one character.")


# 7. Write a Program to take a number of months and print the number of days in that month.

month = int(input("Enter month number (1-12): "))

if month == 2:
    print("February has 28 or 29 days (depending on leap year).")
elif month in (4, 6, 9, 11):
    print("This month has 30 days.")
elif month in (1, 3, 5, 7, 8, 10, 12):
    print("This month has 31 days.")
else:
    print("Invalid month number! Please enter a number between 1 and 12.")

# 8. Write a program to check whether the number is greater than 10 or not

num=int(input("Enter your number :"))

if num >10 :
    print("number is greater than 10 ")
else:
    print("it less than 10 ")


# 9. Write a program to check whether the input character is a vowel or a consonant

ch = input("Enter :")

if ch in "aeiouAEIOU":

    print("it is vowel")
else:
    print("it not")


# 10. WAP that determines whether a given input year is a leap year or not

year=int(input("Enter year:-"))

if year % 4==0 and year % 100 !=0:
    print(year,"is leap year")
else:
    print(year,"not leap year")












