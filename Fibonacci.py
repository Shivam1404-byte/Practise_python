print("Fibonacci Series : ")

def Fibonacci(n):
    n1 = 0
    n2 = 1
    for i in range(n):
        print(n1,end=" ")
        n1,n2 = n2,n1+n2
    print("")

print("Enter no. of fibnacci series : ")
n = int(input())

Fibonacci(n)

