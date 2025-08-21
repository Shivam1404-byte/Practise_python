print("Check wether the string is Palindrome or not ")

def Reverse(str):
    return str[::-1]

print("Enter the word to check wether the String is palindrome or not : ")
str = input()

rev = Reverse(str)

if (str.lower() == rev.lower()):
    print(str,"is palindrome")
else:
    print(str,"is not palindrome")