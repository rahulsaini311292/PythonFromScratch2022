"""
    Numbers and Operators
"""



# Addition

number_1 = 10
number_2 = 15
result = None

print(result)
result = number_1 + number_2
print("Sum= ", result)

addn = 1 + 2

"""
    1. Variables define
    2. = is assignment operator
    3. None  means a value which is nothing.
    4. print() is a function. result inside print is called arguments/parameters.
    5. Addition of two variables of same type (int). 
    6. Operand in our case is number_1 and number_2 means any variable/ value used with an operator.
    7. Arith: +,-,*,/,%,//
"""

# subtraction

number_1 = 10
number_2 = 5

result = number_1 - number_2

print("Sub= ", result)


# Multiply

number_1 = 10
number_2 = 5

result = number_1 * number_2

print("Mul= ", result)


# Divide

number_1 = 10
number_2 = 5

result = number_1 / number_2

print("Div= ", result, type(result))


# Floor Division
number_1 = 9
number_2 = 5

result = number_1 // number_2

print("Floor Div= ", result, type(result))


# Modulus

number_1 = 22
number_2 = 5

result = number_1 % number_2

print("Remainder= ", result, type(result))


# += or -= or *=

fb_like_count = 0
# increment_by = 1
# when clicked 0+1=1,  1+1=2, 2+1=3, 3+1=4......., n+1

fb_like_count = fb_like_count + 1
print("FB like count= ", fb_like_count)
fb_like_count += 1
print("New FB like count= ", fb_like_count)



# example
# 1 m = 100 cm
cm = 100
# BODMAS: Brackets, OF(mul), Divide, Multiply, Add, Sub
meter = int(100/cm)
print(meter)
