"""
    LOOPS
        1. Initialization = Jaha se humari loop start ho
        2. Condition = jaha pe humari loop rukegi
        3. Increment/decrement = humari initial value ko condition se match kavata hai

"""

# print 1 to 10

print(1)
print(2)
print(3)
print(4)
print(5)
print(6)
print(7)
print(8)
print(9)
print(10)

# print 1 to 1000
print("------------------------------------------")

initialization = 1
end = 10

"""
    1. range() is a function
    2. range(initilization, condition, increment)
    3. i is value/ output
    
    for(i=1; i<10; i=i+1)
    {
        printf("we get i inside this loop")
    }
"""
# 10 is exclusive
count = 1
for i in range(1, 11, 1):
    # neeche wale kam ko 10 baar repeat krega
    print(i)
    count = count+1
    # inc_value = 2,3,4,5,6,7,8,9,10,11
    print("temp_count_value", count)

print("count: ", count)


for i in range(1, 11, 1):
    print(i)

# print odd number from 1 to 10
print("odd")
for i in range(1, 11, 2):
    print(i)

print("even")
for i in range(0, 11, 2):
    print(i)


for i in range(1, 100, 33):
    print(i)

# i < 1 : 1<1
for i in range(10, 1, -1):
    print(i)


# linear search




