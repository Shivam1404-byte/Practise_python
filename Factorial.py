print("Factorial of a Number")

def recursiveFact(n):
    if(n == 0 or n == 1):
        return 1
    else:
        return n * recursiveFact(n-1)
    
def iterativeFact(n):
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    return fact


print("Enter the number to find a factorail : ")
n = int(input())

fact = recursiveFact(n)
F = iterativeFact(n)

print("Factorial of number",n,"is",fact)
print("Factorial of number",n,"is",F)