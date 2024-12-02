#censored_words = ['dark', 'sark', 'park', 'hark', 'lark', 'cark', 'mark', 'qark', 'kark', 'nark']
censored_words = input("enter your banned words separated by space: ").lower().split()
user_input = input("enter 5 words separated by space: ").lower().split()

final_output = []

for i in user_input:
    if i in censored_words:
        final_output.append('#!$*')
    else:
        final_output.append(i)

print(final_output)