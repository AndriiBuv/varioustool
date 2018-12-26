
import nltk
from itertools import permutations
from nltk.corpus import words
nltk.download('words')

user_input = input('enter your argument:\n')

spel = [''.join(data) for data in permutations(user_input)]

for i in spel:
    if i in words.words():
        print(i)




