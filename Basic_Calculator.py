print("Basic Calculator")


print("Enter Two numbers : ")
num1 = float(input())
num2 = float(input())

print("Enter the operation to be performed +,-,*,/: ")
ch = input()

res = 0

if ch == '+':
    res = num1+num2
elif ch == '-':
    res = num1-num2
elif ch == '*':
    res = num1 * num2
elif ch == '/':
    if num2 != 0:
        res = num1/num2
    else:
        print("Error:Division by zero is not allowed")
        exit()
else:
    print("Enter the valid operation")
    exit()

print("The result is : ",res)

