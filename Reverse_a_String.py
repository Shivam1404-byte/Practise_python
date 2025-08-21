print("Reverse a string ")

def method1(str):
    return str[::-1]

def method2(str):
    n = len(str)
    rev = ""
    for i in range(n-1,-1,-1):
        rev = rev + str[i]
    return rev

def method3(str):
    left = 0
    right = len(str) - 1
    chars = list(str)
    while(left<=right):
        chars[left],chars[right] = chars[right],chars[left]
        left+=1
        right-=1
    rev = "".join(chars)
    return rev

print("Enter a String : ")
str = input()

rev = method3(str)
print("Reverse of the String is ",rev)