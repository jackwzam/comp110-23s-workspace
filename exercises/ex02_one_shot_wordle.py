"""EX02 - One-Shot Worlde - Loops!"""

__author__ = "730581165"

SECRET: str = "python"
guess: str = input(f"What is your {len(SECRET)}-letter guess? ")
playing: bool = True

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

i: int = 0
boxes: str = ""


while playing:
    if len(guess) != len(SECRET): 
        guess = str(input(f"That was not {len(SECRET)} letters! Try again: ")) 
    else:  # length of word is 6 letters
        while i < len(SECRET):
            if SECRET[i] == guess[i]: 
                boxes = boxes + GREEN_BOX
            elif SECRET[i] != guess[i]:
                n: int = 0
                found: bool = False
                while found is False and n < len(SECRET):
                    if guess[i] == SECRET[n]:  # i is constant and n is changing
                        found = True
                    else:
                        n = n + 1
                if found is True:
                    boxes = boxes + YELLOW_BOX
                else:
                    boxes = boxes + WHITE_BOX
            i = i + 1
        print(boxes)
        playing = False    
if guess == SECRET:
    print("Woo! You got it! ")
    playing = False
else:
    print("Not quite. Play again soon. ")
    playing = False