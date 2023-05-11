import random

def play_game(filename):
    print("What's the word??")

    with open(filename) as file:
        word_list = file.read().split()

    random_word = random.choice(word_list)
    print(random_word)
    
    display = []
    num_letters = len(random_word)
    
    for letter in random_word:
        display.append('_')
    print(display)    

    guesses = 3
    while guesses > 0:
        
        guess = input("guess a letter: ")
        if guess in random_word:
            print(f"correct: {letter}")
            for i in range(len(random_word)):
                if guess == random_word[i]:
                    display[i] = guess
            print(display)
        else:
            guesses -= 1
            print("Nope! You have " + str(guesses) + " guesses left.")
    if guesses == 0:
        print(f"The secret word is: {random_word}")

if __name__ == "__main__":
    play_game("words.txt")