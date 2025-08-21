print("The Largest of three Numbers ")

print("Enter the three Numbers : ")
num1 = int(input())
num2 = int(input())
num3 = int(input())

largest = 0

if num1>num2:
    if(num1 > num3):
        largest = num1
    else:
        largest = num3
else:
    if(num2 > num3):
        largest = num2
    else:
        largest = num3

print("Three numbers are :",num1,num2,num3)
print("Largest of the three numbers is : ",largest)