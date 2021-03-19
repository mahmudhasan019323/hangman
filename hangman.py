import random 
from hangman_art import *
from words import *
import os

#prints the title
print(logo)
#choses a random word from the word list
chosen_word = random.choice(word_list).lower()
#generates list of dashes 
dash = ["_"] * len(chosen_word)
lives = 6
game_over = False
#the loop continue till game_over = False 
while(not game_over):
    print(chosen_word)
    guess = input("guess a letter: ")
    # print('\n')
    os.system('cls' if os.name == 'nt' else "printf '\033c'")
    if dash.count(guess) != 0:
      print(' '.join(dash).upper(),'\n')
      print("you already guessed the letter")
      continue
    for index,letter in enumerate(chosen_word):
        if letter == guess:
            dash[index] = letter
    print(' '.join(dash).upper(),'\n')
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life. lives remaining {lives}")
    print(stages[lives])
    if lives == 0:
        print("you lose")
        game_over = True
    elif not dash.count('_'):
        print("you win")
        game_over = True
