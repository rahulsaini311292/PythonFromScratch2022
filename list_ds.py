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
    4. remove/delete
    5. length of list
    6. update
    7. Extend
    8. Slicing

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




