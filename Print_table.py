'''
5. Print the multiplication table of a given number from n × 1 to n × 10. 
'''
num = int(input("Enter any Number: "))
i = 1
while i <= 10:
    print(num,"*",i,"=",num*i)
    i += 1