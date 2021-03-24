import random

a = random.randint(0, 100)

while True:
    print('Guess the number between 0 and 100!')
    g = input()
    g = int(g)

        if g > a:
            print('Your guess', g, 'is too high. Try again!')
        elif g < a:
            print('Your guess', g, ' is too low. Try again!')
        if g == a:
            print('You found the correct number ', a)
            break