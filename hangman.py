# Simple Hangman game
import random

word_list = ["aardvark", "baboon", "camel"]
display = []

random_word = random.choice(word_list)
for i in range(0, len(random_word)):
    display.append("-")

wrong_guess = 0

while "-" in display and wrong_guess < 5:
    letter = input("Guess the letter: ").lower()
    found = False
    for i in range(0, len(random_word)):
        if random_word[i] == letter:
            display[i] = letter
            found = True
    if not found:
        wrong_guess += 1
    print(display)

if "-" not in display:
    print("you guessed the word:", random_word)
else:
    print("you couldn't guess it, correct word was: ", random_word)
