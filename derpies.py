#!/usr/bin/python
"""
Domo and Fishy code <3
10/5/2017  12:22 AM
"""
import random

def magic_8ball(derp=None):
    """
    This is our really neat baby <3
    """
    # ask them for a question
    answer = raw_input("Ask any question you want yo.")

    # If no variables are passed in...
    if derp:
        # There is no random here, only love <3
        if derp == "does fishy love domo?" or derp == "does domo love fishy?":
            print "yes"
    else:
        if answer:
            random_number = random.randrange(0,6)
            if random_number == 1:
                print "yes"
            elif random_number == 2:
                print "no"
            elif random_number == 3:
                print "maybe"
            elif random_number == 4:
                print "fuck knows mate"
            elif random_number == 5:
                print "ask your mother"
        else: 
            print "I asked for an input yo, what the fuck?"
