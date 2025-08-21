print("Count Vowels and Consonants ")

print("Enter the word to count vowels and consonants : ")
str = input()

cntV=0
cntC=0
vowels = 'aeiou'

for ch in str.lower():
    if ch.isalpha():
        if ch in vowels:
            cntV+=1
        else:
            cntC+=1

print(f"The word {str} has {cntC} consonants and {cntV} Vowels")