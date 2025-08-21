print("Sum of the N natural number ")

print("Enter the number : ")
num = int(input())

sum = 0

for i in range(1,num):
    sum = sum + i

print("The Sum of the first",num,"numbers are : ",sum)