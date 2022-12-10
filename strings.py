"""
    STRINGS: Collection of characters enclosed in quotes.
    1. Loops
    2. Slicing
    3. Linear
    4. Length
    5. Index
    6. Immutable
"""

# empty string
name = ""
name = "Nishant"
print(name)
surname_i = 'J'

print(name + surname_i)

# + operator is used to concat strings - strings k case mai
# + operator is used to add also -  integers k case mai
full_name = name + surname_i
print(full_name)

# index
print(name[0])
print(name[1])
print(name[-1])

# loop
print("---------loop------------")
for val in name:
    print(val)

print("------range loop--------")
name_len = len(name)
# NISHANT
for i in range(0, name_len, 1):
    print(name[i])

# edit string using index
# name[6]="i"

# mylist = [1, 2, 3]
# mylist[0] = 0
# print(mylist)

print(name + "J")
print(name)

# Slicing
# Nishant
print("------Slicing------")
# start: end: update
print(name[0:4:1])
print(name[0:1:1])
print(name[::])
print(name[3::1])
print(name[0:7:2])
print(name[0::2])
print(name[::2])
print(name[1::2])

sentence = "My name is Nishant"

print(sentence[::-1])
# output = "Nishant is name my"
sentence_list = sentence.split()
print(sentence_list)
print(sentence_list[::-1])
# Now List can be updated
"""
    0 - my  ---------- Nishant
    1 - name---------- is
    2 - is------------ name
    3 - Nishant------- my
"""
# len of list is 4 => 3rd index= 4-1
len_of_list = len(sentence_list)
for i in range(0, len_of_list//2, 1):
    # backup to store ith value
    # 0-my, 1-name
    temp_val = sentence_list[i]
    # 0 = sen_list[(4-1)-0]=> sen_list[3]
    # 1 = sen_list[(4-1)-1]=> sen_list[2]
    sentence_list[i] = sentence_list[(len_of_list-1)-i]
    sentence_list[(len_of_list-1)-i] = temp_val

print(sentence_list)

# convert list back top string
sentence = " ".join(sentence_list)
print(sentence)
