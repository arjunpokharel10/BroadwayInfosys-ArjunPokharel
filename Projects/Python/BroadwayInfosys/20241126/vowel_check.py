vowels = ['a', 'e', 'i', 'o', 'u']

word = input("enter a word: ")

for i in word.lower():
    if i in vowels:
        print("the word contains a vowel")
    break 
        

print('it is a vowel' if any(char in vowels for char in word.lower()) else 'it is not a vowel')