print("Print all prime numbers in range")

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
    
def prime_in_range(num):
    prime_num = []
    for i in range(num):
        if check_prime(i):
            prime_num.append(i)

    print("The prime number in the range are : ")
    for i in prime_num:
        print(i,end=" ")

print("Enter the range of prime number : ")
num = int(input())
prime_in_range(num)