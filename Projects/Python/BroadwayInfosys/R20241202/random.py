
string = "this is a dummy text"
string = list(string)
string.reverse()
string = ''.join(string).upper()

count = sum(1 for char in string.lower() if char in 'aeiou')

print(string)
print(f"count: {count} {'vowel' if count == 1 else 'vowels'}")

