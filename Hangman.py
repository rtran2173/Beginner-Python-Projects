import random
import string

from Words import words

def valid(Words):
    word = random.choice(Words) # randomly chooses a word from Words.py
    while '-' in word or ' ' in word: # While condition to take out words with space and dash
        word = random.choice(Words)
    return word.upper()

def hangman():
    word = valid(words)
    word_letters = set(word) # letters in word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() # what the user guessed

    lives = 6

    # getting user input
    while len(word_letters) > 0 and lives > 0:

        # Display used letters
        print('You have', lives, 'lives left and you have used the letters: ', ' '.join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ' '.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        print('---------------------------------------------------------')
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # Takes away one life from a failed attempt
                print('Letter is not in word. Try again.')

        elif user_letter in used_letters:
            print("Already guessed the letter. Type a letter you did not used.")

        else:
            print("Invalid character. Try again.")

    # gets here when len(word_letters == 0 or when lives == 0
    if lives == 0:
        print('No more lives, you lose')
        print('Your word:',word,)
    else:
        print('You have guessed the word',word,)
        print('You won')

hangman()