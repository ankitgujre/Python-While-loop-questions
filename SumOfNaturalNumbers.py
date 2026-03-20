'''
6. Calculate and print the sum of the first n natural numbers. 
'''

# num = int(input("Enter any NUmber: "))
# if num < 0:
#     print("Please enter positive number.")
# else:
#     sum = 0
#     while num > 0:
#         sum += num
#         num -= 1
#     print(sum)


num = int(input("Enter any number: "))

if num < 0:
    print("Please enter positive number.")
else:
    total = num * (num + 1) // 2
    print(total)              #Variable ka naam sum rakhna technically chal jayega, but best practice nahi hai.

# Kyuki Python me sum() ek built-in function bhi hota hai.