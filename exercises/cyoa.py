"""EX06 - Choose Your Own Adventure."""

__author__ = "730581165"


player: str = ""
points: int = 0
NAMED_CONSTANT: str = "\U0001F608"


def main() -> None:
    """Main function that takes user through the entire experience."""
    global points
    global player
    greet() #  enter greeting function and given introduction
    print("There are three places you can check first: 1) Phillips Hall 2) The Pit 3) The Wilson Library Water Fountain.")
    first_location: int = int(input("Would you like to travel to destination 1, 2, or 3? "))
    location: bool = False 
    while location is False: #  making sure a vaild response is entered
        if 1 > first_location or first_location > 3:
            first_location = int(input("That was not a location you could travel to. Try again: "))
        if first_location == 1:
            phillips_probability() #  enter phillips
            print("You decide to first check the pit before checking the other places.")
            the_pit()
            location = True
        if first_location == 2:
            the_pit() #  enter the pit
            print("You decide to first check Phillips Hall before checking the other places.")
            phillips_probability()
            location = True
        if first_location == 3: #  enter wilson library
            print("You traveled to the Wilson Library Water Fountain but found no plus swipes. You drank some water from the fountain to hydrate for your journey and died of lead poisoning.")
            exit()
    print("There are two places you can travel to: 1) Davis Library 2) Kenan Laboratory")
    second_location: int = int(input("Would you like to travel to destination 1 or 2? "))
    location2: bool = False
    while location2 is False: #  making sure a valid response is entered
        if 1 > second_location or second_location > 2: #  invalid response has been entered
            second_location = int(input("That was not a location you could travel to. Try again: "))
        if second_location == 1:
            davis_library()
            print("You now head to Kenan Laboratory.")
            kenan_lab()
            location2 = True
        if second_location == 2:
            kenan_lab()
            print("You now head to Davis Library.")
            davis_library()
            location2 = True
    print("It is rumored that the evil devil is at Kenan Stadium with the remainder of your plus swipes.")
    final_location: bool = False
    answer: str = input(f"{player}, are you brave enough to face the evil blue demon? yes or no? ")
    while final_location is False:
        if answer == "no":
            answer = input("You should really reconsider. Are you brave enough to face the evil blue demon? ")
        if answer == "yes":
            kenan_stadium(points)
            final_location = True
    try_again()



def greet() -> None:
    """Greets user and introduces the game."""
    global player
    player += input("What is your name? ")
    print(f"Greetings {player}, welcome to Chapel Hill!")
    print(f"Listen closely {player}. The evil blue devil has stolen all 35 of your plus swipes and scattered them across campus.")
    print("It is imperative that you retrieve as many of the stolen plus swipes as possible, so you can use them throughout the semester.")
    print("We are currently at the Old Well.")
    print("I have to leave now.")
    print("If the devil were to see me...")
    print("Well uhh...")
    print("Just be careful in your journey to retrieve the stolen plus swipes.")
    print("And good luck!")

def phillips_probability() -> None:
    """Takes user to Phillips Hall to retrieve plus swipes and incoorporates randomness."""
    print("You enter Phillips Hall and encounter a math guru that claims to be a long-lost relative of Ramsey.")
    print("The math guru tells you he possesses 6 of your 35 missing plus swipes, but that he has been cursed by the blue devil.")
    print("The math guru hands you a die. He tells you that the he can only give you the number of plus swipes associated with the number you roll on the die, or he will be permanently banned from UNC basketball games.")
    global points
    import random
    dice_roll: int = random.randint(1,6)
    points += dice_roll
    dice_roll = str(dice_roll)
    print(f"You roll a {dice_roll}.")
    print(f"The math guru hands you {dice_roll} plus swipes and vanishes.")
    print("There is a message on the chalk board behind where the math guru stood that directs you to either the top floor of Davis Library or Kenan Laboratory.")

def the_pit() -> None:
    """Takes user to the pit to retrieve plus swipes."""
    print("You reach the pit and it is empty.")
    print("You see that a sign has been posted and approach the sign.")
    print("On the sign you find 3 plus swipes!")
    global points
    points += 3
    print("The sign reads: You must travel to either the top floor of Davis Library or Kenan Laboratory.")

def davis_library() -> None:
    """Takes user to Davis Library to retrieve plus swipes."""
    print("You have reached the top floor and noticed that the library was empty.")
    print("It suddenly feels cool and you anxiously look around.")
    print("A ghost emerges from the floor and speaks:")
    print("I have haunted this library for decades, and I have been watching you along your journey.")
    print("I see that you are shaking. By the way, let me assure you that I am a friendly ghost. Now that blue devil ... he's evil.")
    print("He hid 4 of your plus swipes in the library, but I collected them for you!")
    print("Please take these plus swipes and be on your way. Watch out for the blue devil.")
    global points
    points += 4
    
def kenan_lab() -> None:
    """Takes user to Kenan Lab to find plus swipes."""
    print("You enter Kenan Laboratory and stumble across a mad scientist.")
    print("The mad scientist looks at you and runs away.")
    response: bool = False
    choice: int = int(input("Do you 1) chase the mad scientist or 2) let him get away: "))
    while response is False:
        if choice < 1 or choice > 2: #  invalid choice
            choice = int(input("That was not a valid choice. Try again: "))
        if choice == 1:
            print("You caught the mad scientist and found 7 plus swipes in his lab coat pocket.")
            global points
            points += 7
            response = True
        if choice == 2:
            print("You let him get away and continue searching Kenan Laboratory.")
            print("After several hours of searching you find nothing and leave the Laboratory.")
            response = True

def kenan_stadium(num: int) -> int:
    print("You enter the stadium and see the evil devil standing in the middle of the field.")
    print(f"The evil devil looks at you and laughs. {NAMED_CONSTANT}")
    print("He then says, 'I see you have found the plus swipes I stole. In order to get the rest...you must defeat me in combat.")
    print("Fortunately for you, the evil devil is totally unskilled and you easily recover the remainder of your missing plus swipes!")
    global points
    points += 14
    print(f"Congratulations! You defeated the evil blue devil and recovered {points} plus swipes!")
    return points


def try_again() -> None:
    answer: str = input("Would you like to play again? ")
    if answer == "yes":
        global points
        global player
        points = 0
        player = ""
        main()
    else:
        print("The End.")

if __name__ == "__main__":
    main()
#plus swipe tally: 21