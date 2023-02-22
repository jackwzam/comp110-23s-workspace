"""Practice writing functions"""

def mimic(my_words: str) -> str:
    """Given the string my_words, outputs same string"""
    return my_words
print(mimic("Hello!"))

def mimic_letter(my_word: str, letter_idx: int) -> str:
    """Outputs the character of my_words at index letter_idx"""
    if letter_idx < len(my_word): #  letter index is valid
        return my_word[letter_idx]
    else:
        print("Too high of an index")