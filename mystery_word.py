import random

def play_game(filename):
    print("What's the word??")

    with open(filename) as file:
        word_list = file.read().split()

    random_word = random.choice(word_list)
    print(random_word)
    display = ''
    # num_letters = len(random_word)
    for letter in random_word:
        display += ' _'
    print(display)

    # user_guesses = ''
    # print(user_guesses)

    guesses = 3
    while guesses > 0:
        wrong_guesses = 0
        display += letter
        letter = input("guess a letter: ")
        for word in random_word:
            if letter in random_word:
                print(f"correct: {letter}")
                break
            else:
                wrong_guesses += 1
                break
    
        if letter not in random_word:
            guesses -= 1
            print("Nope! You have " + str(guesses) + " guesses left.")
        if guesses == 0:
            print(f"The secret word is: {random_word}")

if __name__ == "__main__":
    play_game("words.txt")