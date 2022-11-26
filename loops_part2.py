"""
    LOOPS PART 2
    1. Initialization (Start)
    2. Condition (END)
    3. Increment/decrement (Update Start)

    stop loop when start becomes equal to end
"""
# for(i=0; i<3; i=i+1) -> i=3; 3<3 F : 0,1,2

for i in range(0, 3, 1):
    # 1st loop - i=0: 0<3 T
    # 2nd loop - i=1: 1<3 T
    # 3rd loop - i=2: 2<3 T
    # 4th loop - i=3: 3<3 F
    print(i) # 0, 1, 2


# stop loop when start becomes equal to end
start = 0
end = 3
update = 1
for start in range(start, end, update):
    # 1st loop - i=0: 0<3 T
    # 2nd loop - i=1: 1<3 T
    # 3rd loop - i=2: 2<3 T
    # 4th loop - i=3: 3<3 F
    print(start) # 0, 1, 2

print("==========================")
# 10 is not included
# 1<10, 2<10, 3<10....., 10<10(False)
for val in range(0, 10, 1): # ye loop 10 baar ghumegi i.e 0-9
    print(val)

for val in range(1, 10, 1): # ye loop 9 baar ghumegi i.e 1-9
    print(val)

# print even no from 0 to 10
# for(i=0; i<10; i=i+2)
print("-------------")
count = 0
for val in range(1, 11, 2): # ye loop 10 baar ghumegi i.e 0-9
    print(val)
    # count = count + 1
    count += 1

print("for loop iteration count", count)

# while loop
print("----------While loop-------------")
# start
i = 0
# condition
# for(i=0; i<10; i=i+1)
while i < 10:
    print(i)
    # update(increment)
    i = i+1

"""
    1. Variable
    2. Assignment operator
    3. Loop
    4. Condition
    5. Comparison operator(<=)
    6. Print function
    7. Incrementing j's previous value by 2 in each loop/iteration
    8. total 5 iteration.
"""
j = 0
while j <= 10:
    print(j)
    j = j+2

j = 0
while j <= 4:
    print(j)
    j = j+1

print("-------------------------dsadsadsad-----------------")
end = 100 # database
start = 1
count = 0
# stop loop when start becomes equal or greater to end
while start < end: # 1 < 100,.........., 101 < 100
    print("Do this operation", start)
    # calculate iteration count
    count = count + 1
    start = start + 2

print("total count of iteration", count)


print("-----Electricity Meter Bill----")

"""
    1. Days count = 30 (END)
    2. Starting = 1 (START)
    3. Update = 1 (Increment)
    4. per unit cost = 5
    5. Let per day consumption = 5 units
"""

day_count = 30
start = 0
per_unit_cost = 5
per_day_consumption = 5 # fix
final_consumption = 0 # 5, 10, 15, 20.....150

for _ in range(start, day_count, 1):
    # new_value = prev + constant(per_day_consumption)
    final_consumption = final_consumption + per_day_consumption

print(final_consumption)
print("My Electricity Bill = Rs", final_consumption * per_unit_cost)


