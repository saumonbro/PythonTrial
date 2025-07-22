def sanitize(text):
    """
    Ensure text has only letters and return it in lowercase.
    Ex: aBc -> abc
        ab12 -> ValueError
    """
    if not text.isalpha():
        raise Exception(f"Invalid input. The hangman expects only letters: {text}")
    return text.lower()


def get_guess():
    """
    Prompt the user for a guess. A valid guess is a single letter.
    It is returned in lowercase.
    """
    guess = ""
    while len(guess) != 1 or not guess.isalpha():
        guess = input("Enter a single letter: ").strip()
    return guess.lower()

def clear():
    print("\033[H\033[J", end="") 

def display_state(hidden, attempts_left):
    """
    Util to display the state of the game.
    """
    clear()
    print("Word: " + " ".join(hidden))
    print(f"Tries left: {attempts_left}")
    print()


def play_hangman(answer, max_attempts=10):
    """
    Returns a bool saying if the player wins.
    """
    secret = sanitize(answer)
    hidden = ["_"] * len(secret)
    mistakes = []

    while max_attempts > 0 and "_" in hidden:
        display_state(hidden, max_attempts)
        guess = get_guess()

        if guess in hidden or guess in mistakes:
            print("You already tried " + guess + ".")

        elif guess in secret:
            print("You found the letter " + guess + ".")
            for i in range(len(secret)):
                if secret[i] == guess:
                    hidden[i] = guess
        else:
            print("The letter " + guess + " is not in the word.")
            mistakes.append(guess)
            max_attempts -= 1

    display_state(hidden, max_attempts)
    return max_attempts > 0


def main():
    clear()
    secret_word = input("Enter the answer: ").strip()
    try:
        sanitize(secret_word)
    except Exception as e:
        print(e)
        return

    won = play_hangman(secret_word, max_attempts=10)

    print("You won !" if won else "You lose !")
    print("The word was: '" + secret_word + "'")

if __name__ == "__main__":
    main()
