# age = 20
# price = 19.95
# first_name = "Tomo"
# print(price)

# name = input("What is your name? ")
# print("Hello " + name)

# birth_year = input("Enter your birth year: ")
# age = 2024 - int(birth_year)
# print(age)

# first = input("Type the first number: ")
# second = input("Type the second number: ")

# print("Sum: ", float(first) + int(second))

# course = "Python for beginners"
# print("Python" in course)

# price = 25
# print(price > 10 and price < 30)

# temperatuer = 45

# if temperatuer > 30:
#     print("It's a hot day")
# elif temperatuer > 20:
#     print("It'S a nice day")
# else:
#     print("It's cold")
# print("Done")

# weight = int(input("Weight: "))
# unit = input("K (kg) or L (lbs)")

# if unit.upper() == "K":
#     converted = weight / 0.45
#     print("Weight in lbs: " + str(converted))
# else:
#     converted = weight * 0.45
#     print("Weight in Kg: " + str(converted))

# i = 1

# while i <= 10:
#     print(i)
#     i = i + 1

# numbers = [1,2,3,4,5]
# for item in numbers:
#     print(item)

# numbers = range(5, 10, 3)
# for number in numbers:
#     print(number)


# Python Excercises
# https://www.w3resource.com/python-exercises/python-basic-exercises.php

# print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, \n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are")

# import sys 
# print(sys.version)

# import datetime
# print(datetime.datetime.now())

# from math import pi

# r = float(input("Input the radius of the circle: "))
# area = pi * r * r

# print("The area of the circle is " + str(area))

# first = input("First name: ")
# last = input("Last name: ")
# print(last + " " + first)

# values = input("Please type numbers: ")
# list = values.split(",")
# tuple = tuple(list)

# print(list, tuple)

# filename = input("Input the filename: ")
# f_extns = filename.split(".")
# print(repr(f_extns[-1]))

# color_list = ["Red","Green","White" ,"Black"]

# print("First color: " + color_list[0] + "," + "Last color: " + color_list[-1])

# exam_date = (11,12,2024)
# print("%i, %i, %i" % exam_date)
# print(exam_date[0])

# number = input("Number: ")

# print(number, number)

# n1 = int("%s" % number)
# n2 = int("%s%s" % (number, number))
# n3 = int("%s%s%s" % (number, number, number))

# print(n1 + n2 + n3)

# print(int(number) + int(number + number) + int(number + number + number))

# print(abs.__doc__)

# import calendar

# year = int(input("Input the year: "))
# month = int(input("Input the month: "))

# print(calendar.month(year, month))

# print("""Test message 
# test message 
# test message""")

# from datetime import date

# first_date = date(2012, 7, 2)
# last_date = date(2014, 7, 11)

# delta = last_date - first_date

# print(delta.days)

# from math import pi

# r = 6.0
# v = 4.0/3.0 * pi * r**3

# print(v)

# def difference(n):
#     if n <= 17:
#         return 17 - n
#     else:
#         return (n-17) * 2
    
# print(difference(10))
# print(difference(30))

# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

# print(near_thousand(1000))
# print(near_thousand(800))
# print(near_thousand(2500))
