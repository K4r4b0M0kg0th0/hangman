import random

def get_words_from_file(file):
    try:
        with open(file) as f:
            words = f.read().splitlines()
    except FileNotFoundError:
        print("File not found. Please check the file name and try again.")
    except:
        print("An error occurred. Please try again.")
    return words

def play_again():
    while True:
        play_again = input("Do you want to play again? (y/n)").lower()
        if play_again == "y":
            return True
        elif play_again == "n":
            return False
        else:
            print("Invalid input. Please enter y or n.")

def get_guess():
    guess = input("Guess a letter or type 'clue' for a hint: ").lower()
    if len(guess) == 1:
        return guess
    return None

def hangman():
    difficulty = input("Choose difficulty (easy, medium, hard): ").lower()
    if difficulty == "easy":
        file = "easy_words.txt"
    elif difficulty == "medium":
        file = "medium_words.txt"
    elif difficulty == "hard":
        file = "hard_words.txt"
    else:
        print("Invalid input. Please enter easy, medium or hard.")
        return
    # Get words from file and shuffle them
    words = get_words_from_file(file)
    random.shuffle(words)

    # Select a random word from the list
    word = "".join(words.pop())

    # Create a set to store the user's previous guesses
    guessed_letters = set()

    # Create a variable to store the number of incorrect guesses
    incorrect_guesses = 0

    # Create a variable to store the number of correct guesses
    correct_guesses = 0

    # Create a variable to store the number of blank spaces in the word
    blank_spaces = "_" * len(word)

    # Create a variable to store whether the game is over or not
    game_over = False

    # Create a variable to store the number of clues used
    clues_used = 0

    score = {"name": "", "score": 0}

    hangman_figures = {
        0: "",
        1: "",
        2: "",
        3: "",
        4: "",
        5: "",
        6: "",
    }
    def give_clue():
        nonlocal clues_used, correct_guesses
        if clues_used < 3:
            # Pick a random index of the word
            index = random.randint(0, len(word)-1)
            while word[index] in blank_spaces:
                index = random.randint(0, len(word)-1)
            blank_spaces = blank_spaces.replace(word[index], index, 1)
            print("Here's a clue: The letter at index", index, "is", word[index])
            clues_used += 1
            correct_guesses += 1
        else:
            print("You've used all your clues!")

    def display_word(blank_spaces):
        print("Word: ", blank_spaces)
            
    while not game_over:
        display_word(blank_spaces)

        # Ask the user for their next guess
        guess = get_guess()
        if guess is None:
            if guess == "clue":
                give_clue()
                continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the letter to the set of previous guesses
        guessed_letters.add(guess)

        # Check if the letter is in the word
        if guess in word:
            # Update the blank spaces with the correct letter
            blank_spaces = blank_spaces.replace(guess, blank_spaces, 1)
            correct_guesses += 1
            print("Correct!")
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1
            print("Incorrect. You have", 6 - incorrect_guesses, "guesses left.")
            if incorrect_guesses == 6:
                game_over = True
                print("You lose! The word was", word + ".")
                return
        if correct_guesses == len(word):
            game_over = True
            score["name"] = input("Enter your name: ")
            score["score"] = correct_guesses
            print("You win! The word was", word + ".")
            return

if __name__ == "__main__":
    while True:
        hangman()
        if not play_again():
            break
    print("Thanks for playing!")
