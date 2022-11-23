"""
    When to apply brakes
"""

# string: character or a word or a sentence
apply_brakes = False
# Boolean: True or False
obstacle = False

# while riding no obstacle found
if obstacle == False: # True == False
    print("No need to apply brakes")

if obstacle == True: # False == True
    apply_brakes = True
    print("Apply Brakes:", apply_brakes)


print("Ride Ends!!")

"""
    1. Boolean values use ki hai
        a. True or False
    2. Comparison Operator
        a. == it compares two values or values of variables or variable with variable.
        b. 10 == 10
        c. obstacle == False
        d. count (variable) == new_count(variable)
    3. if condition
        a. mere andar ka code tb tun hoga jab meri conditon True ho jayegi.
    
"""

"""
    print True if condition is False
    1. Print True
    2. if condition is false
"""
print("Second prog starts")
result = True
condition = False

if condition: # if False
    print(" condition is False")
else:
    print(result)


print("Third program Starts")

apply_brakes = False
obstacle = True

if obstacle:
    apply_brakes = True
    print("Apply brakes here")

else:
    print("Smooth Ride")


print("4th program Starts")

hours_count = 10
print("----", hours_count >= 10)
if hours_count >= 10:
    print("Streaming Start")
else:
    print("Notify me")


# Identity Operator
a = 1
b = a

print(a is b)

c = 1
d = 1

print(c is d)

mylist1 = [1, 2, 3]
mylist2 = [1, 2, 3]
print(mylist2 is mylist1)
print(mylist2 == mylist1)

