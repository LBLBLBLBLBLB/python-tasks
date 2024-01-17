import random

secretNum = random.randint(1, 20)
print('I am thinking of a number between 1 and 20.')
print('You have 6 chance to guess number')

for guessTaken in range(1, 7):
    guess = int(input("Take a guess : "))

    if guess < secretNum:
        print('Your guess is too low.')
    elif guess > secretNum:
        print('Your guess is too high.')
    else:
        break

    if guess == secretNum:
        print('Good job! You guessed my number in ' + str(guessTaken) + 'guesses!')
    else:
        print('Nope. The number I was thinking of was ' + str(guessTaken))