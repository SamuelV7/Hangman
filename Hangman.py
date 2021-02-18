import random
the_word = "Welcome"

def hangman(the_word): #Returns true if game is finished
    #setting up the game
    lives = 6
    word_to_guess = the_word.capitalize()
    is_game_finished = False
    user_guess_word = []

    for letter in word_to_guess:
        user_guess_word.append('_')

    while is_game_finished == False:
        if lives == 0:
            print("You are out, you lost")
            is_game_finished = True
            return True

        else:
            print("Guess one of the letters")
            user_input = input(": > ")

            user_input = user_input.capitalize()

            if user_input in user_guess_word:
                print("You have already guessed the word")
            else:
                for letter in word_to_guess:
                    if user_input == word_to_guess[letter]:
                        user_guess_word[letter] == user_input
                        print("Congrats, You got it right")
                    else:
                        print("Wrong youre guess is wrong")
            
hangman(the_word)