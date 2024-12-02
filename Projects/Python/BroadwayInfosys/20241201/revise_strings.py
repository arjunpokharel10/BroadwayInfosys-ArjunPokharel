def string_reversal(words):
    reversed_words = ""
    for i in words:
        reversed_words = i + reversed_words
    return reversed_words


def vowel_count(words):
    vowels = "aeiou"
    num_vowel = 0
    for char in words:
        if char in vowels:
            num_vowel += 1
    return num_vowel

def upperised(words):
    words = words.upper()
    return words

words = "this is a dummy text"

print(string_reversal(words))
print(vowel_count(words))
print(upperised(words))

        
    