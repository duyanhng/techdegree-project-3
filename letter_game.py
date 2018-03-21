import random
import os
import sys

# make a list of words
words = [
    'apple',
    'grape',
    'grapefruit',
    'orange',
    'pineapple',
    'guava',
    'lemon',
    'melon',
    'strawberry',
    'blueberry',
    'banana',
    'mango',
    'coconut' 
]

def clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
        
def draw(bad_guesses, good_guesses, word):
    clear()
    print("The secret word is a name of a fruit!")
    print("Strike: {}/7".format(len(bad_guesses)))
    print('')
    print("Bad Guesses:")
    
    for letter in bad_guesses:
        print(letter, end=', ')
    print('\n\n')
    
    print("Secret Word:")
    for letter in word:
        if letter in good_guesses:
            print(letter, end='')
        else:
            print('_', end='')
    
    print('\n')


def get_guess(guesses):
    
    # take guess
    while True:
        guess = input('Guess a letter: ').lower()
        
        if len(guess) != 1:
            print('You can only guess a single letter')
            
        elif guess in guesses:
            print("You've already guess that letter!")
            
        elif not guess.isalpha():
            print("You can only guess letters!")
            
        else:
            return guess
        
def play(done):
    word = random.choice(words)
    bad_guesses = set()
    good_guesses = set()
    word_set = set(word)

    while True:
        draw(bad_guesses, good_guesses, word)
        guess = get_guess(bad_guesses | good_guesses)
        if guess in word_set:
            good_guesses.add(guess)
            
            if not word_set.symmetric_difference(good_guesses):
                draw(bad_guesses, good_guesses, word)
                print("You win! The secret word is {}".format(word.upper()))
                done = True
        else:
            bad_guesses.add(guess)
            if len(bad_guesses) == 7:
                print("You lose! The secret word is {}".format(word.upper()))
                done = True
        if done:
            play_again = input("Do you want to play again? Y/n: ")
            if play_again != 'n':
                return 
            else:
                sys.exit()

def welcome():
    print("Welcome to Letter Game!!!")
    start = input("Press enter to start or Q to quit: ").lower()
    if start == 'q':
        sys.exit()
    else:
        return
                

done = False


while True:
    clear()
    welcome()
    play(done)
