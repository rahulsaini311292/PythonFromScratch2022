"""
    LIST: Linear DS
        List is a collection of data. List can have any type of data. List is heterogeneous.
            a. string
            b. int
            c. float
            d. list
            e. dict
            f. tuple
            g. set
        Most flexible

    1. Index and negative index
    2. Append(insert new data)
    3. pop (remove 1)
    4. remove/delete/clear
    5. length of list
    6. update
    7. Extend
    8. Slicing
    9. append vs extend

    List vs Array(c, c++)
    Array: Array is a collection of homogeneous data.
    Array's length is fixed means I cannot add new value to below array as it already has 4 values
    str name_arr[16] = ["rahul", "nishant", "ben", "clark","abc","a","b","v","r"]

    Dynamic array:

"""

#empty list
empty_list = []
print(empty_list)

name_list = ["rahul", "nishant", "ben", "clark"]

hetro_list = [1, 2, "rahul", 1.2, {2, 3}]

# get data from list using index
nish_name = name_list[1]
print(nish_name)
print(name_list[3])

print(hetro_list[0])
print(hetro_list[4])
print(hetro_list[-1])

"""
    negative indexing
    starts from -1 and ends at negative length of list
"""

print(name_list[-1])
print(name_list[-2])
print(name_list[-3])
print(name_list[-4])

print(name_list[3] == name_list[-1])

"""
    Length of List
    Append: Insert new value: list mai new values dalna hai but end mai
        1. Add new values at the end.
    POP
"""

age_list = [26, 29, 21, 17, 21, "ten"]
# length is also called Count
# len(age_list)
print(len(age_list))

score_list = [26, 29, 21, 17, 21, 50, 131]
new_score = 16

print(score_list)
# appending value
score_list.append(16)
# appending variable
score_list.append(new_score)
print(score_list)

# Cannot append two variables at same time variable
# score_list.append(47, 67) -> not possible append only needs one argument.
score_list.append(47)
score_list.append(67)
print(type(score_list))
print(score_list)

print("------------------")
# POP
print(score_list[-1])
# 0 is index: NOTE: default index is -1
print(score_list.pop(0))
print(score_list)
print(score_list[-1])

print(score_list.pop(4))

print('---------------')
# index out of range
age_list = [26, 29, 21, 17, 11]
print("index of 21", age_list.index(21))
# print(age_list.pop(6))
# print(age_list[7])

for i in range(0, 4, 1):
    # 0: 5: 21
    # 1: 4: 17
    # 2: 3: 11
    # 3: 2: Error index out of range age_list.pop(2)
    # 4
    print(age_list.pop())


print("----update and clear----")

name_list = ['rahul', 'nishant', 'saini', 'Jambhulkar']

# delete
del name_list

# print(name_list)
name_list = ['rahul', 'nishant', 'saini', 'Jambhulkar']
print(name_list)
# Clear: property of list
name_list.clear()
print("empty list", name_list)
name_list.append("rohit")

print("name list", name_list)

# Update an existing list  using index

name_list.append("neha")
name_list.append("nancy")
name_list.append("ritesh")
print(name_list)

name_list[1] = "abc"
name_list[-1] = 123
print("updated name list", name_list)

# index
print(name_list.index(123))
name_list.append("mno")
name_list.append(123)
print(name_list)
name_list[0] = 123
print(name_list.index(123))

# name_list[10] = "dhsadas"

print("-------Extend and Slicing---------")
# append vs extend
# append adds one value(value, list, set....) at the end of a list
# extend adds list's values to another list
age = [20, 20, 30, 50, 17]
temp_age = [50, 70]
# output: [20, 20, 30, 50, 17, 50, 70]
print(age)
age.extend(temp_age)
print(age)
# age.append(temp_age)
# print(age)

# Slicing
salary = [10000, 100000, 200000, 50000, 90000]
# print(salary[0])
# print(salary[1])
# print(salary[2])
# for i in range(0:3:1)
print(salary[1:5:2])
# print start to end
print(salary[:])
print(salary[-4:])


