# Mr. Hangman!

"Mr. Hangman" is based on the classic Hangman game of old but in Python! Mr. Hangman is a word guessing game where the player has to guess a word by suggesting letters one by one but the player has an option to guess an entire word if they feel lucky. The game allows six attempts to guess a letter or whole word before the player loses. If the player fails to guess the word, the game displays a image of a hanged man, hence the name "Mr. Hangman"

![Website Preview](./assets/images/website-preview.png)

# Features

- **get_word():** This function chooses a random word from the list of words provided in words.py.
![get-word](./assets/images/get-word.png)

- **play(word, username=None):** This function is the main game loop. It takes a username parameter, which is the player's name. If the username is not provided, the game will default to **'None'**. The function initializes the game state and displays the welcome message along with the initial state of the game. The player is then prompted to enter a letter or the whole word. The game checks whether the input is a letter or a word and updates the game state accordingly. If the player guesses the word, the game congratulates the player and asks if they want to play again. If the player runs out of attempts, the game displays the hanged man and reveals the correct word.
![play-word](./assets/images/play-word.png)

- **display_hangman(tries):** This function returns a string that represents the hangman state based on the number of attempts remaining.
![display-triess](./assets/images/display-tries.png)