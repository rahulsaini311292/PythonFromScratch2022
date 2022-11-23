"""
    C prog:
            int number; (initialization) -> this can only save integer values.
            number = 1; (assignment)

    Python Prog:
            number = 1 (initialization and assignment) : int
            number = "one'": string
            number2 = '1' : string
            decimal_number = 1.1: float

            int: 1,2,3,4,5,.....-> non decimal values
            str: 'a' 'rahul' ....-> quotes single or double
            float: decimal numbers 1.2, 1.1, 1000.34, 3.14

"""
number = 1
number2 = "one"
number3 = '1'
decimal_number = 1.1

""" in-built function type"""
# int
print(number, type(number))
# str
print(number2, type(number2))
# str
print(number3, type(number3))
# float
print(decimal_number, type(decimal_number))

# casting/ type casting : Converting one data type to another

print("addition:", number + int(number3))

count = int('10')

# normal string variable
money_count = "1000"
# casting on existing variable
numeric_money = int(money_count)

# fail case
# name = int("rahul")
number_9 = 9
number_9_str = str(number_9)
print(number_9_str, type(number_9_str))
print(number_9, type(number_9))

print(number_9 == number_9_str)


# variables
a = 1
b = a
a = 10
print(a == b)
print(a is b)


