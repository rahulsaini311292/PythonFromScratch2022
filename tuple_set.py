"""
    Tuple and Set
    1. Tuple: Collection of data. Tuple is immutable(not changeable). Ordered.
    2. SET: Collection of data but collection of unique elements. Non-indexable/ Un-ordered.
"""

# initialize

age_tup = ()
print(age_tup)
print(type(age_tup))

del age_tup

# print(age_tup)
age_tup = (20, 33, 21, 19, "six", [19, 22], 19)
print(age_tup)

print(age_tup.index(19))
# what will be the output of this line ?
print(age_tup.count(0))
# create a tuple with one value
name_tup = ("rahul",)
print(type(name_tup))


# SET
name_set = {}
print(name_set)
print(type(name_set))
age_set = {100, 12, 14, 15, 88, 16, 12}
print(age_set)
print(type(age_set))

# how can I get a list with unique elements?
# by converting it into set.

num_list = [1, 2, 3, 4, 5, 9, 7, 8, 1, 2]

# num_list = list(set(num_list))
# casting
num_set = set(num_list)
# casting
num_list = list(num_set)

print(num_list)

age_set.add(1000)
print(age_set)

age_set.clear()
print(age_set)

age_set_1 = {18, 14, 11}
age_set_2 = {1, 2, 5, 18}

# age_set_1.update(age_set_2)
# print(age_set_1)

# union won't work without assignment
new_age_Set = age_set_1.union(age_set_2)
# new_age_set = age_set_1.union(age_set_2)
print(new_age_Set)
