print("Check Armstrong Number ")

def Armstrong(n):
    sum = 0
    while(n!=0):
        num = n%10
        sum = sum + num ** 3
        n = n//10
    return sum

print("Enter a number to check wether the number is Armstrong or not: ")
num = int(input())

num2 = Armstrong(num)

if(num == num2):
    print(num,"is Armstrong number ")
else:
    print(num,"is not a Armstrong number")