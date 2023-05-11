guess = input("guess a letter: ")
        # for word in random_word:
        if letter in random_word:
            print(f"correct: {letter}")    
            break
        else:
            wrong_guesses += 1
            break
    