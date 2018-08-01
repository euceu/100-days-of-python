import random

# Rock, Paper, Scissors

# code for game in eng
def main_game_eng():
    userstateoption = input('Choose one! "rock", "paper", "scissors": ')
    # user chooses rock
    if userstateoption == 'rock':
        compchoice = random.randint(1, 3)
        if compchoice == 1:
            print("rock! it's a draw.")
        elif compchoice == 2:
            print("scissors! you win...")
        elif compchoice == 3:
            print("paper! i win!")
    # user chooses paper
    elif userstateoption == 'paper':
        compchoice = random.randint(1, 3)
        if compchoice == 1:
            print("rock! you win...")
        elif compchoice == 2:
            print("scissors! i win!")
        elif compchoice == 3:
            print("paper! it's a draw.")
    # user chooses scissors
    elif userstateoption == 'scissors':
        compchoice = random.randint(1, 3)
        if compchoice == 1:
            print("rock! you win...")
        elif compchoice == 2:
            print("scissors! i's a draw.")
        elif compchoice == 3:
            print("paper! i win!")
    else:
        print("sorry. i didn't understand that!")

# code for game in ger
def main_game_ger():
    userstateoption = input('wähle! "schere", "stein", "papier": ')
    # user chooses stein
    if userstateoption == 'stein':
        compchoice = random.randint(1, 3)
        if compchoice == 1:
            print("stein! unentschieden.")
        elif compchoice == 2:
            print("schere! du gewinnst...")
        elif compchoice == 3:
            print("papier! ich gewinne!")
    # user chooses papier
    elif userstateoption == 'papier':
        compchoice = random.randint(1, 3)
        if compchoice == 1:
            print("stein! du gewinnst...")
        elif compchoice == 2:
            print("schere! ich gewinne!")
        elif compchoice == 3:
            print("papier! unentschieden.")
    # user chooses schere
    elif userstateoption == 'schere':
        compchoice = random.randint(1, 3)
        if compchoice == 1:
            print("stein! du gewinnst...")
        elif compchoice == 2:
            print("schere! unentschieden.")
        elif compchoice == 3:
            print("papier! ich gewinne!")
    else:
        print("verzeihung, das habe ich nicht verstanden.")


def playing_game_eng():
    main_game_eng()
    ask_for_new_game = input("play again? 'y'/'n' : ")
    if ask_for_new_game == 'y':
        playing_game_eng()
    elif ask_for_new_game == 'n':
        print("game over.")

def playing_game_ger():
    main_game_ger()
    ask_for_new_game = input("nochmal? 'j'/'n' : ")
    if ask_for_new_game == 'j':
        playing_game_ger()
    elif ask_for_new_game == 'n':
        print('Spiel vorbei.')

def new_game():
    choose_language = input('ger / eng : ')
    if choose_language == 'ger':
        playing_game_ger()
    elif choose_language == 'eng':
        playing_game_eng()

new_game()