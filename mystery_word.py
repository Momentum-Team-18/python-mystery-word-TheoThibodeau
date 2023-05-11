import random

def play_game(filename):
    # write code here
    with open(filename) as file:
        word_list = file.read().split()
        # how do i knwo it is selecting the test-word file?
        # test-word(random_selection)
        # close file?
        #
    # GUESSING CODE
    random_word = random.choice(word_list)
    print(random_word)
    display = ''
    for word in random_word:
        display += ' _'
    print(display)
       
    guesses = 3
    while guesses > 0:
        letter = input("guess a letter: ")
        if letter in random_word:
            print('correct')
        else:
            guesses -= 1
            print('nope')
            
    print("game over")





if __name__ == "__main__":
    play_game("test-word.txt")