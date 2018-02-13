#!/usr/bin/python
"""
this is a fursona generator! have fun!
"""
import random

first_name = raw_input("What is your first name?")
last_name = raw_input("What is your last name?")
fave_colour = raw_input("What is your favourite colour?")
jack_hand = raw_input("What hand do you masturbate with?")
gender = random.randrange(0,6)


first_upper = first_name.upper()[0]
last_upper = last_name.upper()[0]


if first_upper == "A":
    print ("You is a Kiwi! Stay away from my Sheep!")
elif first_upper == "B":
    print ("You is a Giraffe! Honk honk!")
elif first_upper == "C":
    print ("You is an Axolotl. Go cut off your hand!")
elif first_upper == "D":
    print ("You is a Horse! Neigh!")
elif first_upper == "E":
    print ("You is a Pigeon! Would you leik some bread?")
elif first_upper == "F":
    print ("You is a Mouse! Have you considered working for Chuck-E-Cheese?")
elif first_upper == "G":
    print ("You is a Dog! Ayyy, yer into pup-play!")
elif first_upper == "H":
    print ("You is a Snake! Don't tempt your wife.")
elif first_upper == "I":
    print ("You is a Panda! Please fuck.")
elif first_upper == "J":
    print ("You is a Dairy Cow! Lactation. ;)")
elif first_upper == "K":
    print ("You is a Cat. Have you considered meowing? :3")
elif first_upper == "L":
    print ("You is a Shark! I'm also into blood.")
elif first_upper == "M":
    print ("You is a Badger! Mushroom! Mushroom!")
elif first_upper == "N":
    print ("You is a Bunny! Having fun writing parking tickets?")
elif first_upper == "O":
    print ("You is a Komodo Dragon! Pseudonecrophilia, all the way!")
elif first_upper == "P":
    print ("You is an Octopus! Consentacles only!")
elif first_upper == "Q":
    print ("You is an Emu! Scourge of Australia!")
elif first_upper == "R":
    print ("You is a Snow Leopard! Get off your high horse!")
elif first_upper == "S":
    print ("You is a Dragon! The knight is coming to rescue you!")
elif first_upper == "T":
    print ("You is a Snow Monkey! Fuck desu ka?")
elif first_upper == "U":
    print ("You is a Turtle! Do you like strawberries?")
elif first_upper == "V":
    print ("You is a Ferret! Do you need a nap?")
elif first_upper == "W":
    print (" You is a Deer! My fucking car!")
elif first_upper == "X":
    print ("You is a Bat. Try out your gravelly voice!")
elif first_upper == "Y":
    print ("You is a Naked Molerat! Let's get Nacos!")
elif first_upper == "Z":
    print ("You is a Penguin! You don't do windows.")
else:
    print ("I asked for your name, not some ASCII macaroni art.")


if last_upper == "A":
    print ("You is black and white!")
elif last_upper == "B":
    print ("You is green and purple!")
elif last_upper == "C":
    print ("You is orange and grey!")
elif last_upper == "D":
    print ("You is grey and blue!")
elif last_upper == "E":
    print ("You is white and pink!")
elif last_upper == "F":
    print ("You is blue and green!")
elif last_upper == "G":
    print ("You is magenta and grey!")
elif last_upper == "H":
    print ("You is red and white!")
elif last_upper == "I":
    print ("You is purple and grey!")
elif last_upper == "J":
    print ("You is turqoise and mint!")
elif last_upper == "K":
    print ("You is black and red!")
elif last_upper == "L":
    print ("You is grey and white!")
elif last_upper == "M":
    print ("You is fuscia and pastel pink!")
elif last_upper == "N":
    print ("You is sky blue and grey")
elif last_upper == "O":
    print ("You is yellow and green!")
elif last_upper == "P":
    print ("You is silver and white!")
elif last_upper == "Q":
    print ("You is olive and mint!")
elif last_upper == "R":
    print ("You is white and violet")
elif last_upper == "S":
    print ("You is violet and grey!")
elif last_upper == "T":
    print ("You is black and turqoise!")
elif last_upper == "U":
    print ("You is red and grey!")
elif last_upper == "V":
    print ("You is yellow and black!")
elif last_upper == "W":
    print ("You is white and silver!")
elif last_upper == "X":
    print ("You is yellow and brown!")
elif last_upper == "Y":
    print ("You is blue and white!")
elif last_upper == "Z":
    print ("You is white and orange!")
else:
    print ("I asked for your name, not some bullshit ASCII art.")


if fave_colour == "Blue":
    print ("You have a horse cock, regardless of species.")
elif fave_colour == "Red":
    print ("You have an eyepatch, dunno if it's for real.")
elif fave_colour == "Violet":
    print ("You have streaks of violet in your hair. Edgy.")
elif fave_colour == "Green":
    print ("You have a missing part of your ear. You brawler you!")
else:
    print ("Your colour is considered invalid by the programmer, you are normal.")


if jack_hand == "Left":
    print ("You have a cunt!")
elif jack_hand == "Right":
    print ("You have a cock!")
else:
    print ("I wanted a hand, not some other appendage.")


if gender == 1:
    print ("You are a boy!")
elif gender == 2:
    print ("You are a girl!")
elif gender == 3:
    print ("You are non=binary!")
elif gender == 4:
    print ("You are a trans-boy!")
elif gender == 5:
    print ("You are a trans-girl!")
