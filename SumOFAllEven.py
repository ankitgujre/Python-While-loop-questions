'''
7. Calculate the sum of all even numbers from 1 up to n. 
'''

num = int(input("Enter number: "))
total = 0
i = 1   # start from 1

while i <= num:
    if i % 2 == 0:   # check if even
        total += i
    i += 1           # move to next number

print("Sum of even numbers up to", num, "is:", total)