print("Swapping without temp variable")


print("Enter two numbers : ")
a = int(input())
b = int(input())

print("value of a is ",a," and b is ",b)

a = a+b
b = a-b
a = a-b

print("value of a is ",a," and b is ",b)