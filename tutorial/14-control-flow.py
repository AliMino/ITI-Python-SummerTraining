# if, elif & else

# if True:
#     print('Yes')

# if False:
#     print('No')


# if False:
#     print('Yes')

# else:
#     print('No')


# grade = 75

# if 100 >= grade >= 85:
#     print('Excellent')
# elif 85 > grade >= 75:
#     print('Very Good')
# elif 75 >= grade >= 65:
#     print('Good')
# elif 65 > grade >= 50:
#     print('Passed')
# else:
#     print('Failed')

# grade = 75

# if 100 >= grade >= 85:
#     print('Excellent')

# if 85 > grade >= 75:
#     print('Very Good')

# if 75 >= grade >= 65:
#     print('Good')

# if 65 > grade >= 50:
#     print('Passed')

# if 50 > grade:
#     print('Failed')

########################################################

# For loop

# lst = [ 1, 2, 3, 4 ]

# doubles = []

# for number in lst:
#     doubles.append(2 * number)

# print(lst)
# print(doubles)

# word = 'Hello'

# for char in word:
#     print(char)

# names = [
#     'ahmed',
#     'mohammed',
#     'ali'
# ]

# capitalized_names = []

# for name in names:
#     capitalized_names.append(name[0].upper() + name[1:])

# print(capitalized_names)

##########################################

# Nested loops

# numbers = []

# for i in range(1, 3):
#     for j in range(4, 6):
#         numbers.append(i * j)

# print(numbers)

##########################################

# person = {
#     'name': 'Ali Kamel',
#     'job': "Software developer",
#     'age': 31,
#     'favorite_programming_langugages': [
#         'Python',
#         'Java'
#     ]
# }

# for key, value in person.items():
#     print('{}\t=\t{}'.format(key, value))

# Loop through file's lines

# input_file = open('tutorial/input.txt')

# for line in input_file.readlines():

#     print('"' + line + '"')

# input_file.close()

##########################################

# While loop

# x = 0

# while x < 10:
#     print(x)
#     x += 1

# print(x)


# input_file = open('tutorial/input.txt')

# line = input_file.readline()

# while len(line):

#     print(line)
#     line = input_file.readline()

# input_file.close()

##########################################

# # Early breaking

# input_file = open('tutorial/input.txt')

# for line in input_file.readlines():

#     if 'stop\n' == line:

#         break
    
#     elif 'skip\n' == line:

#         continue

#     print(line)

# input_file.close()

##########################################

# input_file = open('tutorial/input.txt')

# line = input_file.readline()

# while len(line):

#     if 'stop\n' == line:

#         break
    
#     elif 'skip\n' == line:

#         line = input_file.readline()
#         continue

#     print(line)

#     line = input_file.readline()

# input_file.close()

################################################

# names = [
#     'ahmed',
#     'mohammed',
#     'ali'
# ]

# for index in list(range(len(names))):
    
#     name = names[index]
    
#     names[index] = name[0].upper() + name[1:]

# print(names)

# for index, name in list(enumerate(names)):
    
#     names[index] = name[0].upper() + name[1:]

# print(names)

################################################

# names = [ 'Ahmed', 'Mohammed', 'Ali' ]
# scores = [ 100, 90, 80 ]

# for name, score in zip(names, scores):
    
#     print(f'{name} got {score}')

############################################

# Other usages of the 'in' keyword

# course_scores = [ 100, 90, 80 ]

# if 100 in course_scores:

#     print('We have a winner!')

# dictionary = {
#     'k1': 1,
#     'k2': 2,
#     'k3': 3,
# }

# print('k1' in dictionary)
# print('k4' in dictionary)

# print(1 in dictionary.values())
# print(4 in dictionary.values())

# print('h' in 'hello')
# print('H' in 'hello')

############################################

# # Retireve a unique sublist from the following list

# numbers = [ 1, 2, 3, 1, 2, 3 ]

# unique_list = []

# for number in numbers:

#     if (number not in unique_list):

#         unique_list.append(number)

# print(unique_list)

############################################

# List comprehension

# word = 'Hello'

# chars = []

# for char in word:

#     chars.append(char)

# print(chars)

# print(
#     [ char.upper() for char in word ]
# )

# even_numbers = [ num * 2 for num in range(10) if num < 5 ]

# print(even_numbers)


# List comprehension - Nested loops

print([ i * j for i in range(1, 3) for j in range(4, 6) ])
