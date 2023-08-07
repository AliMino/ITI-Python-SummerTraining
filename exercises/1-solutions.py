# Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

# name = input('What\'s your name? ')

# age = int(input('What\'s your age now? '))

# print('Hello', name)
# # print('Hello {}'.format(name))
# # print('Hello {_1}'.format(_1=name))
# # print(f'Hello {name}')

# print('You will a 100 years old at {}'.format(2023 + (100 - age)))

##########################################################################################

# Ask the user for a number. If the number is even, print 0, and if the number is odd, print 1.

# num = int(input('Enter a number: '))

# print(num % 2)

##########################################################################################

# Write a program to accept a string from the user and display characters that are present at an even index number.

# string = input('Enter a string: ')

# print(string[1::2])
# print(string[::2])

##########################################################################################

# print('Twinkle, twinkle, little star,')
# print('      How I wonder what you are!')
# print('          Up above the world so high,')
# print('          Like a diamond in the sky.')
# print('  Twinkle, twinkle, little star,')
# print('      How I wonder what you are')

# print('Twinkle, twinkle, little star,')
# print('\tHow I wonder what you are!')
# print('\t\tUp above the world so high,')
# print('\t\tLike a diamond in the sky.')
# print('  Twinkle, twinkle, little star,')
# print('\tHow I wonder what you are')

##########################################################################################

# Write a Python program that calculates the area of a circle based on the radius entered by the user.

# radius = float(input('Enter the radius of the circle: '))

# area = radius ** 2 * 22 / 7

# print('The area of a circle having the radius {r} is {a}.'.format(r = radius, a = area))

##########################################################################################

# Write a python program that calculates the total seconds from hours, minutes, seconds and milliseconds.

# hours        = float(input('Enter hours: '))
# minutes      = float(input('Enter minutes: '))
# seconds      = float(input('Enter seconds: '))
# milliseconds = float(input('Enter milliseconds: '))

# total_seconds = hours * 3600 + minutes * 60 + seconds + milliseconds / 1000

# print('The total seconds in {h} hours, {m} minutes, {s} seconds and {l} milli-seconds are {S}'.format(
#     h = hours,
#     m = minutes,
#     s = seconds,
#     l = milliseconds,
#     S = total_seconds
# ))

##########################################################################################

# Write a python program that uses summation, subtraction, multiplication, division, exponent, and modulo (all of the basic math operations) to print the number `-1537.24`. Hint: Work backwards from `-1537.24`.

# print(4 * 10 ** 2 / 2 - 1837.24 + 100 % 101)

##########################################################################################

# Write a Python program that accepts an integer (n) and computes the value of n + nn + nnn.

# n = input('Enter an integer: ')

# print(n)
# print(n * 2)
# print(n * 3)

# print(int(n) + int(n * 2) + int(n * 3))

################################################################################################################
################################################################################################################

# # Write a program to accept a string from the user and remove characters starting from zero up to 3 (inclusive) and prints the remaining string.

# whole_string = input('Write a string: ')

# print(whole_string[4:])
# ############################ print('The length of', whole_string, 'is', len(whole_string))

################################################################################################################

# # Here Document
# print(
# """
# I'm a little penguin, black and white
# I waddle to the left,           and I waddle to the right
# When I'm feeling hungry,
#     splash and splish,
#         I jump in the water,
#             and catch a fish!
# """
# )

# print("I'm a little penguin, black and white\nI waddle to the left,\t\tand I waddle to the right\nWhen I'm feeling hungry,\n    splash and splish,\n\tI jump in the water,\n\t\tand catch a fish!")

# print("{line_1}\n{line_2}\n{line_3}\n{line_4}\n{line_5}\n{line_6}".format(
#     line_1 = "I'm a little penguin, black and white",
#     line_2 = "I waddle to the left,\t\tand I waddle to the right",
#     line_3 = "When I'm feeling hungry,",
#     line_4 = "    splash and splish,",
#     line_5 = "\tI jump in the water,",
#     line_6 = "\t\tand catch a fish!"
# ))

# line_1 = "I'm a little penguin, black and white"
# line_2 = "I waddle to the left,\t\tand I waddle to the right"
# line_3 = "When I'm feeling hungry,"
# line_4 = "    splash and splish,"
# line_5 = "\tI jump in the water,"
# line_6 = "\t\tand catch a fish!"

# print(f"{line_1}\n{line_2}\n{line_3}\n{line_4}\n{line_5}\n{line_6}")

################################################################################################################

# # Write a python program that converts celsius tempratures to fahrenheit. (f = 32 + 1.8 * c)

# celsius = float(input('Enter a temperature in celsius: '))
# print('{} degrees celsius are equivelant to {} degrees fahernheit'.format(celsius, 32 + 1.8 * celsius))

################################################################################################################

# # Write a Python program that finds a number’s square root, as well as its square.

# n = 100

# from math import sqrt

# print('The square of {num} is {sq}, and the square root is {sqrt}'.format(
#     num = n,
#     sq = n ** 2,
#     # sqrt = n ** 0.5
#     sqrt = sqrt(n)
# ))

################################################################################################################

# # Given the word `Hello`, write a Python program to print only the letter `e` using indexing (bonus: with two different methods).

# print('Hello'[1])

# string = 'Hello 7mada'

# print(string[ 1 - len(string) ])



