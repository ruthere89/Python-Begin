import random
import time
import string
from word_list import pos_word

# ignore this chunk
used = ["Are you simple? You used that already, try again.", "Of all the letters, you chose the same ones...",
        "You done diddy tried that there letter before.",
        "I see, because a letter you picked previously can be in there more? Try again", "No, try again.",
        "Seriously? Didn't you do that already?"]
you_lose = ["Whomp, whomp. Sorry sport, you lose.", "What a day you're having, huh? Feel that loss, did ya?",
            "So close, yet... well you get it", "You'll get em next time, right?",
            "If it makes you feel any better I am dead on the inside... But your character is dead on the outside."]
good_guess = ["Excellent!", "Excelsior!", "Bravo!", "I wish I were as smart as you!",
              "A light bulb isn't as bright as you!", "Feel good about yourself, you should.",
              "We're having fun, aren't we?", "**Happy Dance**", "Party like you actually won something."]
win_quote = ["Well, that was worth it! Good job!", "Ya did it like you were gettin paid. NICE", "Tres Bien!",
             "Do people stop you on the street to tell you about your genius? They should.",
             "Well, I owe someone money now, didn't think you would do it, but you did.",
             "Congrats, you have won a silly game.", "I do hope Brian doesn't see how smart you are. He really cares.",
             "Is that a happy dance I see?"]
invalid = ["You silly bean, that's not a letter.", "HEY, what game are you playing here?",
           "Huh, wanna try again Sparky?", "ERROR INVALID CHOICE", "So close, guess an actual letter this time.",
           "Did you mean to type that? Again, try again.", "Which alphabet are you using?, Try again."]
not_in_there = ["Not in the word, sorry.", "Tough break, try another one.",
                "Hmmmmmmm...That does not appear to be in this particular word.",
                "OH NO, another attempt has just been wasted.", "One less try, one less letter.",
                "If I were you, I would at least try to guess the correct letters.",
                "Did you graduate primary school? This is a game, but come on and use that big kid brain."]


# Get a worthwhile word
def word_select(pos_word):
    blasphemy = random.choice(pos_word)
    while "-" in blasphemy or " " in blasphemy:
        blasphemy = random.choice(pos_word)
    return blasphemy.upper()


# oof the hard stuff, and that's not what she said...
def delta_vari():
    estos_palabra = word_select(pos_word)
    letras = set(estos_palabra)
    palabre_letras = set(string.ascii_uppercase)
    usado_letras = set()
    oh_noes = 9  # because cats have nine so why shouldn't we
    this_thing = True

    hangman_thing = [""" __
|  |
|  ☺
| /|\.
| / \.
|
======""",
                     """ __
|  |
|  ☺
| /|\.
| / 
|
======""",
                     """ __
|  |
|  ☺
| /|\.
| 
|
======""",
                     """ __
|  |
|  ☺
| /|
|
|
======""",
                     """ __
|  |
|  ☺
| /
|
|
======""",
                     """ __
|  |
|  ☺
|
|
|
======""",
                     """ __
|  |
|
|
|
|
======""",
                     """ __
|
|
|
|
|
======""",
                     """ _
|
|
|
|
|
======""",
                     """
|
|
|
|
|
======"""]
    while len(letras) > 0 and oh_noes > 0:
        print("you have " + str(oh_noes) + " attempts remaining")
        time.sleep(0.25)
        print("Previously on 'Whoever you are played a game'...: ", " ".join(usado_letras))
        time.sleep(0.25)
        previously_on = [letter if letter in usado_letras else "▓" for letter in estos_palabra]
        print("Currently the word looks like this: ", " ".join(previously_on))
        time.sleep(0.25)
        # spanish, because why not
        mira_aki = input("Yo, gimme a letter: ").upper()
        if mira_aki in palabre_letras - usado_letras:
            usado_letras.add(mira_aki)
            if mira_aki in letras:
                letras.remove(mira_aki)
                print(random.choice(good_guess))
                time.sleep(1)
            else:
                oh_noes = oh_noes - 1
                print(random.choice(not_in_there))
                time.sleep(1)
        elif mira_aki in usado_letras:
            print(random.choice(used))
            time.sleep(1)
        else:
            print(random.choice(invalid))
            time.sleep(1)
        print(hangman_thing[oh_noes])
    if oh_noes == 0:
        print(random.choice(you_lose), "The word we were looking for was " + str(estos_palabra) + ".")
    else:
        print("The word was " + str(estos_palabra).upper() + ".")
        print(random.choice(win_quote))

    yes_list = ["yes", "y"]
    thiss = input("Would you like to play again? Yes/Y or No/N: ").lower()
    if thiss in yes_list:
        delta_vari()
    else:
        print("Thank you for playing, I hope you had fun.")
        time.sleep(1.5)
        exit()


delta_vari()
