print("Check the number is Prime or not ")

def check_prime(num):
    cnt = 0
    for i in range(2,num):
        if (num%i==0):
            cnt += 1
            break
    if(cnt == 1):
        return False
    else:
        return True
    
print("Enter the number to check : ")
num = int(input())

if(check_prime(num)):
    print(num,"is a prime Number")
else:
    print(num,"is not a prime number")