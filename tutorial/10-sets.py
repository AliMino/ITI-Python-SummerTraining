

my_list = [ 1, 2, 3 ]
my_set = set(my_list)

print(my_list)
print(my_set)

# Sets are mutable

my_list.append(5)
my_set.add(5)

print(my_list)
print(my_set)

my_list.append(5)
my_set.add(5)

print(my_list)
print(my_set)

text = 'I love apples'

print(set(text))
