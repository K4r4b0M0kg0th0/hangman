import random

def get_words_from_file(file):
    with open(file) as f:
        words = f.read().splitlines()
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

def hangman():
    # Get words from file and shuffle them
    words = get_words_from_file("words.txt")
    random.shuffle(words)

    # Select a random word from the list
    word = words.pop()

    # Create a list to store the user's previous guesses
    guessed_letters = []

    # Create a variable to store the number of incorrect guesses
    incorrect_guesses = 0

    # Create a variable to store the number of correct guesses
    correct_guesses = 0

    # Create a variable to store the number of blank spaces in the word
    blank_spaces = "_" * len(word)

    # Convert the blank spaces variable to a list to update it later
    blank_spaces_list = list(blank_spaces)

    # Create a variable to store whether the game is over or not
    game_over = False

    # Create a variable to store the number of clues used
    clues_used = 0

    def give_clue():
        nonlocal clues_used, correct_guesses
        if clues_used < 3:
            # Pick a random index of the word
            index = random.randint(0, len(word)-1)
            while word[index] in blank_spaces_list:
                index = random.randint(0, len(word)-1)
            blank_spaces_list[index] = word[index]
            print("Here's a clue: The letter at index", index, "is", word[index])
            clues_used += 1
            correct_guesses += 1
        else:
            print("You've used all your clues!")

    while not game_over:
        # Print the current state of the word with blank spaces and guessed letters
        print("Word: ", " ".join(blank_spaces_list))

        # Ask the user for their next guess
        guess = input("Guess a letter or type 'clue' for a hint: ").lower()

        if guess == "clue":
            give_clue()
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You already guessed that letter. Try again.")
            continue

        # Add the letter to the list of previous guesses
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess in word:
            # Update the blank spaces with the correct letter
            for i in range(len(word)):
                if word[i] == guess:
                    blank_spaces_list[i] = guess
                    correct_guesses += 1
            print("Correct!")
        else:
            # Increment the number of incorrect guesses
            incorrect_guesses += 1
            print("Incorrect. You have", 6 - incorrect_guesses, "guesses left.")
            if incorrect_guesses == 6:
                game_over = True
                print("You lose! The word was", word + ".")
        if correct_guesses == len(word):
            game_over = True
            print("You win! The word was", word + ".")

if __name__ == "__main__":
    while True:
        hangman()
        if not play_again():
            break
    print("Thanks for playing!")