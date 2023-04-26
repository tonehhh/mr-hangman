import random
from words import word_list # contains list of words for the game in words.py


def get_word():
    # selects a random word from word_list
    word = random.choice(word_list)
    return word.upper()


def play(word, username=None):
    if not username:
        username = input("Please eneter your username: ")
        print(f"Welcome {username}! Let's play Mr. Hnagman!")

    # creates the initial state of the game
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    # prints the welcome message and initial game state
    print(display_hangman(tries))
    print(word_completion)
    print("\n")

    # loops until teh user either guesses the word or runs out of tries
    while not guessed and tries > 0:
        guess = input("Please guess a letter or word: ").upper()
        
        # checks if the guess is a letter
        if len(guess) == 1 and guess.isalpha():
            # checks if the letter has already been guessed
            if guess in guessed_letters:
                print("You already guessed that letter", guess)
            # checks if the letter is in the word
            elif guess not in word:
                print(guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            # updates the game state with correctly guessed letter
            else:
                print("Good job,", guess, "is in the word!")
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = "".join(word_as_list)
                if "_" not in word_completion:
                    guessed = True

        # checks if the guess is a word
        elif len(guess) == len(word) and guess.isalpha():
            # checks if the word has already been guessed
            if guess in guessed_words:
                print("You've already guessed the word", guess)
            # checks if the word is not the correct word
            elif guess != word:
                print(guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            # updates the game with the correctly guessed word
            else:
                guessed = True
                word_completion = word

        # invalid guess
        else:
            print("Not a valid guess.")
            tries -= 1
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

        # checks the game state after each game
        if guessed:
            print(f"Congrats {username}! You guessed the word! You Win!")
        elif tries == 0:
            print(display_hangman(tries))
            print(f"Sorry {username}, you ran out of tries. The word was " + word + ". Better luck next time!")
        else:
            print("You have", tries, "tries left.")
            print(display_hangman(tries))
            print(word_completion)
            print("\n")

    print("\n")

    replay = input("Would you like to play again? (Y/N)").upper()

    if replay == "Y":
        play(get_word(), username=username)
    else:
        print(f"Thanks for playing {username}!")


# this function returns a string that represents the hangman state based on number of tries remaining
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


# this function runs the Mr. Hangman game
def main():
    
    # prints the Mr. Hangman title
    print("""
  __  __        _  _
 |  \\/  |_ _   | || |__ _ _ _  __ _ _ __  __ _ _ _
 | |\\/| | '_|  | __ / _` | ' \\/ _` | '  \\/ _` | ' \\
 |_|  |_|_|(_) |_||_\\__,_|_||_\\__, |_|_|_\\__,_|_||_|
                              |___/
    """)
    
    # gets a random word for the game
    word = get_word()
    
    # starts the game
    play(word)
    
if __name__ == "__main__":
    main()
