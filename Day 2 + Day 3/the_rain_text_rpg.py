# Python text rpg

import cmd
import textwrap
import sys
import os
import time
import random

screen_width = 100

#### title screen ####

def title_screen_selection():
    option = input("> ")
    if option.lower() == ("play"):
        start_game()
    elif option.lower() == ("help"):
        help_menu()
    elif option.lower() == ("exit"):
        sys.exit()
    else:
        print("type: 'play, help or exit.")
        title_screen_selection()


def title_screen():
    os.system('clear')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print('      ***** The Rain *****      ')
    print(' ´ ´ ´ ´ ´  - play - ´  ´ ´ ´ ´ ')
    print('  ´ ´ ´ ´ ´ - help - ´ ´ ´ ´ ´  ')
    print(' ´ ´ ´ ´ ´  - exit -  ´ ´ ´ ´ ´ ')
    print('  ´ ´ ´ ´ ´          ´ ´ ´ ´ ´  ')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    title_screen_selection()


def help_menu():
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print('         ** help menu **        ')
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    print('  type your commands to do them ')
    print('                                ')
    print('         !enjoy the game!       ')
    print('                                ')
    print("   back                 start   ")
    print('´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´´')
    exit_help_menu = input("> ")
    if exit_help_menu == "back":
        title_screen()
    elif exit_help_menu == "start":
        start_game()
    else:
        help_menu()


#### choices #####

def ch1_option_close_her_eyes():
    print("Close her eyes? y/n                    ")
    option_close_eyes = input("> ")
    if option_close_eyes.lower() == "y":
        print("I close her eyes.                   ")
    elif option_close_eyes.lower() == "n":
        print("I decide to not mess with the scene.")
    else:
        ch1_option_close_her_eyes()


def ch1_option_check_id():
    print("Check ID? y/n                      ")
    option_check_id = input("> ")
    if option_check_id.lower() == "y":
        print("I check her ID.                ")
        time.sleep(2)
        print("Her name is Elizabeth Garcia.  ")
        time.sleep(2)
        print(" 28. Comes from...             ")
        time.sleep(3)
        print("I'm unable to read further.    ")
        time.sleep(1)
        print("'Why were you here, Elizabeth?'")
    elif option_check_id.lower() == "n":
        print("...                            ")
    else:
        ch1_option_check_id()


def ch1_option_check_purse():
    print("Check purse? y/n                       ")
    option_check_purse = input("> ")
    if option_check_purse.lower() == "y":
        print("Inside is a velvet lipstick,       ")
        time.sleep(2)
        print("keys, ...                          ")
        time.sleep(2)
        print("and an ID!                         ")
        time.sleep(1)
        print("But where's her phone?             ")
        ch1_option_check_id()
    elif option_check_purse.lower() == "n":
        print("I shouldn't touch the crime scene. ")
    else:
        ch1_option_check_purse()


def ch1_option_check_body():
    print("Check the body...? y/n                     ")
    option_check_body = input('> ')
    if option_check_body.lower() == 'y':
        print("                                       ")
        print("I try to stand up. The pain is over-   ")
        print("whelming and my body feels sore,       ")
        time.sleep(2)
        print("but I manage to limp over to her.      ")
        time.sleep(2)
        print("I check her pulse                      ")
        time.sleep(2)
        print("and confirm what I expected earlier    ")
        time.sleep(3)
        print("... she's dead.                        ")
        time.sleep(3)
        ch1_option_close_her_eyes()
        time.sleep(3)
        print("She's been stabbed multiple times.     ")
        time.sleep(2)
        print("Her black dress is drenched in blood   ")
        print("and embracing her body.                ")
        time.sleep(2)
        print("Next to her body lies a purse.         ")
        ch1_option_check_purse()
    elif option_check_body.lower() == "n":
        print("I shouldn't touch the crime scene.     ")
    else:
        ch1_option_check_body()

        ### intro ###

def ch1_intro():
    print('***** The Rain *****                           ')
    print("                                               ")
    print("[?]: 'Pain...                                  ")
    time.sleep(3)
    print("      Why does it hurt so much?'               ")
    time.sleep(3)
    print('                                               ')
    print('I see my blood-tainted hand                    ')
    print("softly being kissed by the pouring rain.       ")
    print('                                               ')
    time.sleep(3)
    print("[?]: 'Where am I?                              ")
    time.sleep(1)
    print("      ...Wait.                                 ")
    time.sleep(3)
    print("      Who... am I?'                            ")
    time.sleep(3)
    print('                                               ')
    print('Panic starts to rush through my veins,         ')
    print("where confusion once had made itself a home.   ")
    print('                                               ')
    time.sleep(5)
    print('     "Calm down"                               ')
    time.sleep(2)
    print('                                               ')
    print('I hear those words repeated in sync            ')
    print("with my heartbeat, that feels more like        ")
    print("a monotone sound than an actual pulse.         ")
    print('                                               ')
    time.sleep(5)
    print('                                               ')
    print("After calming down a bit,                      ")
    print("I start inspecting the scenery.                ")
    print('                                               ')
    time.sleep(5)


def ch1_check_scenery():
    print("I check...                                     ")
    print(" a) in front of me.                            ")
    print(" b) behind me.                                 ")
    option_check_scenery = input("> ")
    if option_check_scenery.lower() == "a":
        print("In front of me are trees, I suspect I'm    ")
        print("in a forrest, it's night, and...           ")
        time.sleep(3)
        print("...                                        ")
        time.sleep(2)
        print("...                                        ")
        time.sleep(2)
        print("..?!                                       ")
        time.sleep(2)
        print("A young woman, in her late 20s,            ")
        print("lies in front of me.                       ")
        time.sleep(3)
        print("Her eyes stare into my soul...             ")
        time.sleep(3)
        print("asking...                                  ")
        time.sleep(3)
        print("There's nothing I could answer her         ")
        time.sleep(5)
        print("... she's dead.                            ")
        time.sleep(3)
        ch1_option_check_body()
        print("Behind me is a street.                     ")
        time.sleep(2)
        print("The lights are flickering.                 ")
        time.sleep(2)
        print("No signs. No houses.                       ")
        time.sleep(2)
        print("Just the forrest and me... Great.          ")
        time.sleep(2)
    elif option_check_scenery.lower() == "b":
        print("Behind me is a street.                     ")
        time.sleep(2)
        print("The lights are flickering.                 ")
        time.sleep(2)
        print("No signs. No houses.                       ")
        time.sleep(2)
        print("I decide to inspect what's in front of me. ")
        time.sleep(2)
        print("I'm in a forrest. It's night, and...       ")
        time.sleep(3)
        print("...                                        ")
        time.sleep(2)
        print("...                                        ")
        time.sleep(2)
        print("..?!                                       ")
        time.sleep(2)
        print("A young woman, in her late 20s,            ")
        print("lies in front of me.                       ")
        time.sleep(3)
        print("Her eyes stare into my soul...             ")
        time.sleep(3)
        print("asking...                                  ")
        time.sleep(3)
        print("There's nothing I could answer her         ")
        time.sleep(5)
        print("... she's dead.                            ")
        time.sleep(3)
        ch1_option_check_body()
    else:
        ch1_check_scenery()


def ch1_outro():
    print("Suddenly something sends cold shivers down     ")
    print("my spine, as if death wanted to kiss me        ")
    print("good night – the calm before the storm.......  ")
    time.sleep(3)
    print("...")
    time.sleep(3)
    print("*** TO BE CONTINUED...? ***")


def start_game():
    ch1_intro()
    ch1_check_scenery()
    ch1_outro()


def the_rain():
    title_screen()


the_rain()
