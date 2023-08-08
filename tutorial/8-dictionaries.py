
# Differences between lists and dictionaries:
#   Appearace: lists are declared using [], while dictionaries are declared using {}
#   Items access: list's items are access via their indices, while dictionaries are accessed by keys (names)
#   Mutability: Both lists and dictionaries are mutable.
#   Writing time: Lists are way faster than dictionaries in storing data.
#   Reading time: Dictionaries are the fastest data structure ever for data retrieval.
#   Items' ordering: Lists can be sorted, while dictionaries can not.

person = {
    'name': 'Ali Kamel',
    'job': "Software developer",
    'age': 31,
    'favorite_programming_langugages': [
        'Python',
        'Java'
    ]
}

print(person['name'])
print(person['favorite_programming_langugages'][0].lower())

print(person.keys())
print(person.values())
print(person.items())

[
    (),
    (),
    (),
    (),
    (),
    (),
]
