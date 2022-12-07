"""
    DICT: Collection of key-value pair.
    Unique key leni padti hai



"""

# empty dict
my_dict = {}
print(my_dict)
print(type(my_dict))

del my_dict

# {key:value}
my_dict = {
    "name": "rahul",
    "age": 29,
    "occupation": "SE"
}
print(my_dict)

# how to get value from dict?
print(my_dict['name'])
print(my_dict['age'])
print(my_dict["occupation"])

"""
    Keys are unique and unchangeable(immutable)
    1. Tuple
    2. String
"""
my_second_dict = {
    (1, 2): "rahul",
    (3, 4): "Mickey"
}

print(my_second_dict)

# my_third_dict = {
#     [1, 2]: "rahul",
#     [3, 4]: "Mickey"
# }
#
# list is mutable i.e changeable
# print(my_third_dict)

del my_dict

my_dict = {
    "name": "rahul",
    "age": 29,
    "occupation": "SE",
    "name": "Mickey",
}

# data lost ki problem
print(my_dict)

# clear

print("-------Clear-----------")
my_dict.clear()
print(my_dict)

# GET
my_dict = {
    "name": "rahul",
    "age": 29,
    "occupation": "SE"
}

# get
print(my_dict['name'])
# print(my_dict['names'])
print("-----GET----")
print(my_dict.get('name'))
print(my_dict.get('age'))
print("-----GET Key that do not exists--")
print(my_dict.get('names'))

# update a dict
# add new key-val pair
my_dict['color'] = "red"
# update existing key-val pair
my_dict['name'] = "Mickey"
print(my_dict)

