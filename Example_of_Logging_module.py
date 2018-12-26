
import logging

logging.basicConfig(filename='guess.txt', level=logging.DEBUG, format='%(asctime)s-%(levelname)s-%(message)s')
logging.debug('starting program')

import random
guess = ''
while guess not in ('heads', 'tails'):
    print('Guess the coin toss! Enter heads or tails:')
    guess = input()
toss = random.randint(0, 1) # 0 is tails, 1 is heads
logging.debug(toss)
if toss == guess:
    print('You got it!')
else:
    print('Nope! Guess again!')
    guess = input()
    if toss == guess:
       logging.debug(guess)
       print('You got it!')
    else:
        print('Nope. You are really bad at this game.')
logging.debug('end of program')
