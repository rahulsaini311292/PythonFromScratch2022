"""
    Data Structures: Store date in a particular manner. So that it is easily available when needed.
    Indexing, (key: value)
            1. List (Linear): changeable
                1. get/search using index
                2. update/delete using index
                3. Insert new data
            2. Tuple (Linear): unchangeable
                1. get/search
            3. Set (Linear) (indexing exception because it is unordered)
            4. Dictionary (key: value)
            5. String :  "Rahul", "a", "1", 'nishant', 'b', '2'
"""

age1 = 15
age2 = 13
age3 = 15
age4 = 18
age5 = 18

# List
age_list = [15, 13, 15, 18, 18, 20]
    # mutable-> Changeable
print(age_list)

# Tuple
age_tuple = (15, 13, 15, 18, 18, 20)
    # immutable-> Unchangeable
print(age_tuple)

# Set
age_set = {15, 13, 15, 18, 18, 20}
    # unique elements, Unordered
print(age_set)

"""
    Indexing
    1. starts from 0
    2. Ends = length of Linear DS - 1
        Ex. below salaries => length=5 
            Ends = 5-1 = 4 
    3. Indexing helps to get/search a value from DS in one step.
        a. Indexing also helps to remove/delete data from DS in once step.
        b. Indexing also helps to update data from DS in once step.
        
    4. Sno.  | Position (Indexing)   | value
        1.   | 0th position          | 10000
        2.   | 1st position          | 24000
        3.   | 2nd position          | 15000
        4.   | 3rd position          | 150000
        5.   | 4th position          | 200000
"""
print("--------------------------")
salaries = [10000, 24000, 15000, 150000, 200000]
print(salaries)
print(type(salaries))
# how to get value from list using index
rahul_salary = salaries[3]
print(rahul_salary)

office_boy_salary = salaries[0]
print("ofc_boy_salary=", office_boy_salary)


# un-indexable
set_roll_no = {1, 20, 30, 4, 5}
print(set_roll_no)
print(type(set_roll_no))


my_tup_rollno = (1, 2, 3, 4, 5)
print(my_tup_rollno)
print(type(my_tup_rollno))
print(my_tup_rollno[3])
print(my_tup_rollno[1])













