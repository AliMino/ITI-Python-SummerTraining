# String indexing

# String Slicing

text = 'Hello'

# String indexing

# print(text[0])
# print(text[1])
# print(text[-1])
# print(text[-2])

# String Slicing

# print(text[0:])
# print(text[1:])
# print(text[:-2])
print(text[0:2:1])
print(text[0:3:2])
print('123456789'[::2])
print('123456789'[1::2])

# Querying string length

print(len('abcef'))
print(len('   '))
print(len('\n'))

# Usefull string methods

print('Hello'.lower())
print('Hello'.upper())
print('I love Python'.split()[2])
print(type('I love Python'.split()))
print('I--love--Python'.split('--'))

# Formatting strings

lang = 'Python'

print('I love', lang)
print(f'I love {lang}')
print('I love {} and {}'.format('Python', 'PHP'))
print('I use python version {php_ver} and PHP version {py_ver}'.format(py_ver=3.6, php_ver=8.1))

# Here document

print(
"""
Hello world
    Hi back


            Python 3.6
"""
)
