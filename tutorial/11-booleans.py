
# print(type(True))
# print(type(False))

# print('True & True is', True and True)
# print('True & False is', True and False)
# print('False & True is', False and True)
# print('False & False is', False and False)

# print('==========================================')

# print('True or True is', True or True)
# print('True or False is', True or False)
# print('False or True is', False or True)
# print('False or False is', False or False)

# print('==========================================')

# print('The complement of True is', not True)
# print('The complement of False is', not False)


def return_yes():
    print('yes')
    return True

def return_no():
    print('no')
    return False

print(return_yes() and return_no())
print(return_no() and return_yes())

print(return_yes() or return_no())
print(return_no() or return_yes())
