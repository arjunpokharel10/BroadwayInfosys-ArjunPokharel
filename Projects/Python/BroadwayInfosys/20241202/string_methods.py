text = "python is fun to learn"




text = text.split(' ')

text.append('wow')

text.extend(['yes', 'it', 'is'])

text = ' '.join(text)


print(text)
print(type(text))

print(sum(text.count(i) for i in 'aeiou'))