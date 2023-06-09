import random
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

def play_game(filename):
    print(Fore.LIGHTYELLOW_EX + "What's the word??")

    with open(filename) as file:
        word_list = file.read().split()
        easy_mode = []
        normal_mode = []
        hard_mode = []
        random_word = random.choice(word_list)
        # define lists for each type of word difficulty
        
        for word in word_list:
            if len(word) >= 4 and len(word) <= 6:
                easy_mode.append(word)
            elif len(word) >= 6 and len(word) <= 8:
                normal_mode.append(word)
            else:
                hard_mode.append(word)
        # write a loop that iterates the words and organizes them based on length
        # and puts the randomly chosen word into its specific list
        
        easy_word = random.choice(easy_mode)
        normal_word = random.choice(normal_mode)
        hard_word = random.choice(hard_mode)
        # defines variables that contain lists with different levels of difficulty
        choose_level = str(input(Back.LIGHTYELLOW_EX + Fore.BLACK + "Choose level of difficulty (Easy, Normal, or Hard): "))
        
        if choose_level == "Easy":
            random_word = easy_word
        if choose_level == "Normal":
            random_word = normal_word
        if choose_level == "Hard":
            random_word = hard_word
        # assign difficulty level to corresponding mode
    
    display = []
    # num_letters = len(random_word)
    
    for letter in random_word:
        display.append('_')
    print(display)    

    guesses = 8

    while guesses > 0:
        guess = input(Style.BRIGHT + Fore.LIGHTCYAN_EX + "guess a letter: ")
        if guess in random_word:
            print(f"correct: {guess}")
            for i in range(len(random_word)):
                if guess == random_word[i]:
                    display[i] = guess
            print(display)
        else:
            guesses -= 1
            print(Fore.LIGHTYELLOW_EX + "Nope! You have " + str(guesses) + " guesses left.")
    if guesses == 0:
        print(Style.BRIGHT + Fore.RED + Back.BLACK + "GAME OVER!")
        print(Style.BRIGHT + Fore.LIGHTCYAN_EX + f"The secret word is: {random_word}")
        print(Style.BRIGHT + Fore.LIGHTYELLOW_EX + "Do you want to play again? (y/n)")

if __name__ == "__main__":
    play_game("words.txt")