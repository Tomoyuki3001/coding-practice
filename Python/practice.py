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

# Exercise 17
# def near_thousand(n):
#     return ((abs(1000 - n) <= 100) or (abs(2000 - n) <= 100))

# print(near_thousand(1000))
# print(near_thousand(800))
# print(near_thousand(2500))

# def sum_numbers(x, y, z):
#     sum = x + y + z
#     if x == y == z:
#         sum = sum * 3
#     return sum

# print(sum_numbers(1,2,3))
# print(sum_numbers(2,2,2))

# def new_string(text):
#     if len(text) >= 2 and text[:2] == "Is":
#         return text
#     else:
#         return "Is" + text
    
# print(new_string("Array"))
# print(new_string("IsArray"))

# def larger_string(text, n):
#     result = ""
#     for i in range(n):
#         result = result + text

#     return result

# print(larger_string("test", 2))
# print(larger_string("py", 3))

# def list_count(nums):
#     count = 0

#     for num in nums:
#         if num == 4:
#             count = count + 1
    
#     return count

# print(list_count([1,2,3,4,5,4,4]))

# def check_vowel(text):
#     all_vowels = "aiueo"

#     return text in all_vowels

# print(check_vowel("c"))
# print(check_vowel("e"))

# def check_array(numbers_array, num):
#     return num in numbers_array

# print(check_array([1,2,3,4,5],3))
# print(check_array([1,2,3,4], -3))

# def histgram(items):
#     for n in items:
#         output = ""
#         times = n
#         while times > 0:
#             output += "@"
#             times = times -1
        
#         print(output)

# histgram([3,4])

# def concatenate_list(list):
#     result = ""

#     for element in list:
#         result += str(element)

#     return result

# print(concatenate_list([1,4,5,6]))

# numbers = [11,245,664,354,567,456,237,456,453,224,987]

# for x in numbers:
#     if x == 237:
#         print(x)
#         break
#     if x % 2 == 0:
#         print(x)

# color_list_1 = set(["White", "Black", "Red"])
# color_list_2 = set(["Red", "Green"])

# print(color_list_1.difference(color_list_2))

# Exercise 30
# base = int(input("Input the base: "))
# height = int(input("Input the height: "))

# print("Area is: ", base * height / 2)

# def gcd(x, y):
#     gcd = 1

#     if x % y == 0:
#         return y
    
#     for k in range(int(y / 2), 0, -1):
#         if x % k == 0 and y % k == 0:
#             gcd = k
#             break
#     return gcd

# print("GCD of 12 and 17 =", gcd(4, 6))

# def sum_numbers(x, y, z):
#     sum = 0
#     if x == y or x == z or z == y:
#         return sum
#     else:
#         return x + y + z
    
# print(sum_numbers(3,4,3))

# def sum_numbers(x,y):
#     sum = x + y
#     if sum in range(15, 20):
#         sum = 20

#     return sum

# print(sum_numbers(8, 2))

# def check_numbers(x,y):
#     if x == y:
#         return True
#     if (x + y) == 5 or abs(x - y) == 5:
#         return True
#     else:
#         return False

# print(check_numbers(8,3))

# def add_numbers(a, b):
#     if not (isinstance(a, int) and isinstance(b, int)):
#         return "Inputs must be integers!"
    
#     return a + b

# print(add_numbers(10, 20.1))

# name = input("Your name: ")
# age = input("Your age: ")
# ahand = input("Your hand is: ")

# print("{}\n{}\n{}".format(name, age, ahand))

# def squared_numbers(x, y):
#     return (x+y)**2

# print(squared_numbers(2,3))

# def calculate_rate(amount, int, years):
#     future_value = amount * ((1 + (0.01 * int)) ** years)
#     return future_value

# print(round(calculate_rate(10000, 3.5, 7), 2))

# Exercise 40
# import math

# p1 = [4, 0]
# p2 = [6, 6]

# distance = math.sqrt(((p1[0] - p2[0]) ** 2) + ((p1[1] - p2[1]) ** 2))
# print(distance)

# import os.path

# print(os.path.exists("practice.py"))

# import struct

# print(struct.calcsize("P") * 8)

# import site
# print(site.getsitepackages())

# import multiprocessing

# cpu = multiprocessing.cpu_count()

# print(cpu)

# for i in range(0, 10):
#     print("K", end="")

# print("\n")


