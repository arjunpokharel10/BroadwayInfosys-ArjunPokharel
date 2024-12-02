options = ['aarav', 'aayush', 'bikram', 'aaron', 'adam', 'arjun']


# output = []

# for s in options:
#     if len(options) <= 1:
#         continue            #this check is to see if the length of the string is more than 1 char, if it is not, then no point going forward. 

#     if s[0] != 'a':
#         continue

#     if s[-1] != 'n':
#         continue

#     output.append(s)
# print(output)


################################################################################################
#list comprehension method

output = [s for s in options if len(s) > 1 if s[0] == 'a' if s[-1] == 'n']

print(output)