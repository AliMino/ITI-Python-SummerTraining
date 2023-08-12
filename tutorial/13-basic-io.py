
# # Absolute path
# # From the highest level on disk -> to the file location

# # Relative path
# # from current location -> to file location

input_file = open('tutorial/input.txt')

# # print(input_file.read())
# # print('==================')

# # input_file.seek(0)

# # print(input_file.read())

# print(input_file.readlines())

# print(input_file.readline())

# print('-------------')

# print(input_file.readline())

# print('-------------')
# input_file.seek(0)
# print(input_file.readline())

# input_file.close()
# #####################################

# # Automatically-closed files!

# input_file = open('tutorial/input.txt')

# File openning modes
#   r   -> read only (default)              r+  -> read & write
#   w   -> overwrite or create              w+  -> read & overwrite or create
#   a   -> append only

with open('tutorial/input.txt', mode='r+') as input_file:

    contents = input_file.read()
    input_file.seek(0)
    
    print(input_file.write(contents + ' tail'))

