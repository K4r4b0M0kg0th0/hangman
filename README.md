# Hangman Game

### Welcome to the Hangman game! In this game, you will be given a word and you will have to guess the letters in the word.

## How to Play

- Start the game by running the hangman.py file.
- Choose a difficulty level (easy, medium, hard). The difficulty level will determine the
- list of words that the game will choose from.
- The game will randomly select a word from the list.
- You will be prompted to guess a letter.
- If the letter is in the word, it will be revealed in the correct position.
- If the letter is not in the word, you will lose a guess.
- You can also type 'clue' to get a hint about the word. You have a maximum of 3 clues to use during the game.
- The game ends when you have correctly guessed the word or when you have used all your guesses.
- At the end of the game, you will be prompted to play again.

## Tips

- Keep track of the letters you have already guessed to avoid guessing the same letter multiple times.
- Try to guess the most common letters first (e.g. e, a, o, i, etc.).
- Use clues wisely, as they can be very helpful but you have limited number of clues.

## Requirements

- Python 3.x
- The game uses the random and open modules, which should be included in a standard Python installation.

## Note

- The words used in the game are stored in text files, easy_words.txt, medium_words.txt and hard_words.txt.
- If the file is not found, the program will prompt the user with a message "File not found. Please check the file name and try again."
- If there is any other error, the program will prompt the user with a message "An error occurred. Please try again."
Thanks for playing and good luck!