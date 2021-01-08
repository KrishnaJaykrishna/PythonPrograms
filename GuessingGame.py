import random
rand = random.randint(1,9)
chances = 0
while (chances<5):
    guess = int(input('Enter Your Guess'))
    if (guess==rand):
        print('Congratulations You Won')
        break
    elif (guess<rand):
        print ('Youre guess is low')
    else:
        print ('Youre Guess Is High')
    chances = chances+1
if (chances >=5):
    print ('You Lost')
