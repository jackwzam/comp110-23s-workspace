"""EX03 - Structured Wordle"""

__author__ = "730581165"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def contains_char(word: str, char: str) -> bool:
    """Given a word and character, and the character is searched for in the word"""
    assert len(char) == 1
    i: int = 0
    found: bool = False
    while found is False and i < len(word):
        if char == word[i]:
            found = True
        else:
            word_idx += 1
    return found        

def emojified(guess: str, secret: str) -> str:
    """Assigns a color to each character of the guess based on if the character matches, is found in the word, or is not found in the word"""
    assert len(guess) == len(secret)
    i: int = 0
    boxes: str = ""
    while i < len(secret):
        if guess[i] == secret[i]:
            boxes += GREEN_BOX
        else:
            if contains_char(secret, guess[i]):
                boxes += YELLOW_BOX
            else:
                boxes += WHITE_BOX
        i += 1
    return boxes

def input_guess(expected_length: int) -> str:
    """Given an integer and compares the length of the user's guess to the integer"""
    correct: bool = False
    guess: str = input(f"Enter a {expected_length} character word: ")
    while correct is False:
        if len(guess) == expected_length:
            correct = True
        else: 
            guess = input(f"That wasn't {expected_length} chars! Try again: ")
    return guess

def main() -> None:
    """The entrypoint of the program and main game loop."""
    turn: int = 1
    SECRET: str = "codes"
    playing: bool = True
    while playing is True and turn < 7:
        print(f"=== Turn {turn}/6 ===")
        guess: str = input_guess(len(SECRET)) #  ensures guess is the appropriate number of characters
        print(emojified(guess, SECRET)) #  assigns the appropriate color emoji box to each character
        if guess == SECRET: #  user has won
            return print(f"you won in {turn}/6 turns!")
        else: #  user advances to next turn
            turn += 1
    return print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main()