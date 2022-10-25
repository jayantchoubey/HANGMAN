import random
from words import words
import string

#choosing a word
def getWord(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:   #in case of a '-' or space, we find another word
        word = random.choice(words)
    return word.upper() #change all cases to uppercase

def hangman():
    word = getWord(words)
    letters_word = set(word)    #letters in the word
    alphabets = set(string.ascii_uppercase) #all english alphabets
    used_letters = set()    #letters that have been guessed

    #number of lives a user has
    lives = 7
    #getting user input
    while len(letters_word) > 0 and lives > 0:

        #giving the user his status
        print(f'You have {lives} lives left. You have used these letters: ', ' '.join(used_letters))
        wordlist = [letter if letter in used_letters else '-' for letter in word]
        print('\nCurrent word: ', ' '.join(wordlist))

        #asking user to give a letter
        user_letter = input("\nGuess a letter: ").upper()
        if user_letter in alphabets - used_letters:
            used_letters.add(user_letter)
            if user_letter in letters_word:
                letters_word.remove(user_letter)
                print('')

            #reducing lives for wrong attempt
            else:
                lives = lives - 1
                print("\nIncorrect guess!!!")
        
        elif user_letter in used_letters:
            print('\nYou already used that character, try again!!!')
        
        else:
            print('\nPlease enter a valid character.')

    #die if no lives are left
    if lives == 0:
        print('\nYou died. The word was ', word)
    
    #won the game
    else:
        print(f'\nCongrats!!! You guessed the word {word} correctly.')

if __name__ == '__main__':
    hangman()