char = input("enter a word/phrase etc.: ")

left, right = 0, len(char)-1

is_palindrome = True

while left < right:
    if not char[left] == char[right]:
        is_palindrome = False
        break
    left += 1
    right -= 1

print(f" {'is plaindrome' if is_palindrome else 'not palindrome'}")