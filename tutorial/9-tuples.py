# Tuples are immutable lists.

#  Lists -> []
#  Dictionaries -> {}
#  Tuples -> ()

# Declaring tuples

tup = (1, 2, 3, 2)
# tup = ('',)

# print(type(tup))

# Retrieving the length of a tuple

# print(len(tup))

# Accessing tuple items

# print(tup[0])
# print(tup[1])
# print(tup[2])
# print(tup[-1])
# print(tup[-2])
# print(tup[-3])

# Shared behavior with lists

# print(tup.count(1))
# print(tup.count(2))
# print(tup.count(3))
# print(tup.count(4))

# print(tup.index(2, 2))

# Tuples are IMMUTABLE

# tup[0] = 4

# converting tuples to lists

lst = list(tup)

print(tup)
print(lst)

lst[0] = 4
