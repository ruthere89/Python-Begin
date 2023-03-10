# catch them imports
import random
import time

# explain rules
print("Rock paper scissors: AVATAR the Last Airbender version")
time.sleep(2)
print("Opposites will cancel each other out resulting in a tie, the same as choosing the same as your opponent.")
time.sleep(4)
print("Rules are based on the Avatar cycle, not the actual bending ability (ridiculous!). Air - Water - Earth - Fire")

# define outcomes due to the tie variables being numerous, tedious, but better than crazy
ciskle = {"air": "a", "water": "w", "earth":"e", "fire":"f"}
search_skl = dict((b, d) for d, b in ciskle.items())
def defeats(user, opponent):
    cork = {}
av_rps = {
    "air": {"air": "Draw", "water": "Win", "earth": "Zen", "fire": "Loss"},
    "water": {"air": "Loss", "water": "Draw", "earth": "Win", "fire": "Zen"},
    "earth": {"air": "Zen", "water": "Loss", "earth": "Draw", "fire": "Win"},
    "fire": {"air": "Win", "water": "Zen", "earth": "Loss", "fire": "Draw"}
}
def a_win():

# while loop to keep it going
while True:
    # define variables and selections
    choice = ["air", "water", "earth", "fire"]
    user_choice = input("Which element will you choose? ").lower()
    computer_choice = random.choice(choice)
    # run game defining program with exceptions
    print("You played " + user_choice.title())
    if user_choice == "avatar":
        print("LOL, you tried.")
    elif user_choice in choice:
        print("Your opponent has played " + computer_choice.title())
        print("We have a " + av_rps[user_choice][computer_choice])
    else:
        print("You cannot play " + user_choice + " please try again using the elements of the Avatar's cycle.")
    #would player like to continue?
 #add definition for extra function to close loop better
    conti = input("Continue playing? Y/N: ").lower()
    if conti == "n":
        break
    elif conti == "y":
        continue
    else:
        print("That was never an option, try again...")


        #things to add!