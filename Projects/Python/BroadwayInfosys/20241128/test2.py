import random

# create a list of animes
animes = [
    ['naruto', 'pephype', 'forever', 'series'],
    ['haikyuu', 'sports', 'short', 'series'],
    ['mushishi', 'chill', 'short', 'series'],
    ['march comes in like a lion', 'slice of life', 'short', 'series'],
    ['attack on titan', 'a movie', 'a series', 'short']
]

# input mood
print('what mood are you in?')
mood = input()

# loop through and find a matching mood
for item in animes:
    for item[1] == mood:
        print(f"{mood} anime: {[item[0]]}")