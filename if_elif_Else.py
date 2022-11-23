"""
    If-> Agar True hai tabhi if k andar wala code run hoga

    if-> Agar True hai tabhi if k andar wala code run hoga
    else-> Agar  if False  hai tabhi else k andar wala code run hoga


    IF -> Agar True hai tabhi if k andar wala code run hoga
    ELIF-> Agar True hai tabhi elif k andar wala code run hoga
    ELSE-> Agar  if false  and elif false hai tabhi else k andar wala code run hoga


    If
    elif
    elif
    elif...
    else

"""
# Comparison Operators
print(1 < 2)
print(1 > 2)

if 1 < 2:
    print("Yes 1 is less than 2")

if 3 > 2:
    print("Yes 3 is greater than 2")

if 5 > 4:
    print("4 is greater than 5!!!")
else:
    print("I am a loser!!!")

# employee_count = 41 # ye data database ye aya hai
# is_my_company_a_startup = True
#
# # print(41>=100)
# print(employee_count >= 100)
#
# if employee_count >= 100:  # False
#     print("My company is not a startup now")
#     is_my_company_a_startup = False
#     # database mai maine iss new data ko save krr diya
# else:
#     print("My Company is still a startup.")


#  ===============================================
print(" ===============================================")
""" 
    1. Startup - <= 5000000 lakh funding
    2. Established Startup- 1 cr to 10 cr funding
    3. MNC - 10 cr se zda funding hai
"""

funding = 100000001

print(funding >= 5000000)
print(funding <= 100000000)

if funding <= 5000000:
    print("Startup")

# AND/ OR is logical operator
elif funding >= 5000000 and funding <= 100000000:
    print("Established Startup")

else:
    print("MNC")

#  ===============================================
print(" ===============================================")
""" 
    Divide students based on their percentage
    1. total sections : 4 (A, B, C,D)
    2. percent: 85% >= A
                      65% to 85% > B
                      45% to 65% > C
                      35% to 45%> D    
                           
"""

percentage = 99

if percentage < 0 or percentage >= 101:
    print("Invalid Input")

# nested if else
else:
    # nested code
    if percentage >= 85 and percentage <= 100:
        print("Go to A Section")
        if 1 <= 1:
            if 2 >= 2:
                if 2 == 1:
                    print("hi")
                else:
                    print("bye")

    elif percentage >= 65 and percentage < 85:
        print("Go to B Section")

    elif percentage >= 45 and percentage < 65:
        print("Go to C Section")

    elif percentage >= 35 and percentage < 45:
        print("Go to D Section")

    else:
        print("Failed")
