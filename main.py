# coding=utf-8

#########################################
####### COMPLETE PYTHON BOOTCAMP ########
# Milestone Project 1: Tic Tac Toe Game #
# Author: Jonatan Borrego del Pozo      #
# Date: March 2017                      #
#########################################


#########################################
# IMPORTS:                              #
#########################################
import os
import sys


#########################################
# CLASSES:                              #
#########################################
class bcolors:
    PINK = '\033[95m'
    GREEN = '\033[92m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'


#########################################
# FUNCTIONS:                            #
#########################################

# Function that detects OS you are running
def check_os():
    from sys import platform as _platform

    if _platform == "linux" or _platform == "linux2":
        return('linux')
    elif _platform == "darwin":
        return ('mac')
    elif _platform == "win32":
        return ('windows')

# Function that clean the screen
def clear_screen():
    if check_os() == 'linux' or check_os() == 'mac':
        os.system('clear')  # Linux & Mac OS x
    elif check_os() == 'windows':
        os.system('cls')    # Windows

    # Another way to do it:
    # from IPython.display import clear_output
    # clear_output()

# Function that Draws Game Board with current Game status
def draw_board(gamestatus):
    print '\n\t', bcolors.BOLD, 'TIC TAC TOE GAME\n', bcolors.ENDC
    print '\t ',gamestatus[1],' | ',gamestatus[2],' | ',gamestatus[3],' '
    print '\t-----------------'
    print '\t ', gamestatus[4], ' | ', gamestatus[5], ' | ', gamestatus[6], ' '
    print '\t-----------------'
    print '\t ', gamestatus[7], ' | ', gamestatus[8], ' | ', gamestatus[9], ' '
    print '\n'

# Function that reset the Game
def reset_game():
    clear_screen()
    gamestatus = ('X',
                  ' ', ' ', ' ',
                  ' ', ' ', ' ',
                  ' ', ' ', ' ')
    draw_board(gamestatus)
    return gamestatus

# Function that makes a movement
def play(gamestatus):
    position = 0

    print bcolors.GREEN, 'Turn for', gamestatus[0],'', bcolors.ENDC
    while position == 0:
        position = raw_input('Insert box you want to check (1-9): ')
        if position in ('1', '2', '3', '4', '5', '6', '7', '8', '9'):
            # Cast position to Integer
            position = int(position)

            # Cast gamestatus to List
            gamestatus = list(gamestatus)

            # Check position availability in gamestatus
            if check_availability(gamestatus, position):
                # Check position with current Player
                gamestatus[position] = gamestatus[0]
                # Change player turn
                if gamestatus[0] == 'X': gamestatus[0] = 'O'
                else: gamestatus[0] = 'X'
            else:
                position = 0
                print 'Position selected is already in use'
        else:
            position = 0
            print 'You have to select a position between 1 and 9'

        clear_screen()
        draw_board(gamestatus)
    return gamestatus

# Function that checks if Game is already finished
def is_game_finished(gamestatus):
    finished = False

    if winner(gamestatus, 'X'):     # Check if Player X won the game
        print 'Player X won the Game'
        finished = True
    elif winner(gamestatus, 'O'):   # Check if Player O won the game
        print 'Player X won the Game'
        finished = True
    elif tie(gamestatus):           # Check if game was tied
        print 'The Game was tied'
        finished = True

    return finished

# Function that checks if Player won the game
def winner(gamestatus, player):
    won = False

    # Check all possible combinations
    if (gamestatus[1] == gamestatus[2] == gamestatus[3] == player) or \
        (gamestatus[4] == gamestatus[5] == gamestatus[6] == player) or \
        (gamestatus[7] == gamestatus[8] == gamestatus[9] == player) or \
        (gamestatus[1] == gamestatus[4] == gamestatus[7] == player) or \
        (gamestatus[2] == gamestatus[5] == gamestatus[8] == player) or \
        (gamestatus[3] == gamestatus[6] == gamestatus[9] == player) or \
        (gamestatus[1] == gamestatus[5] == gamestatus[9] == player) or \
        (gamestatus[3] == gamestatus[5] == gamestatus[7] == player): won = True

    return won

# Function that checks if Game Board is already full and Players tied
def tie(gamestatus):
    # True if all list is filled
    # False if any box unckecked
    return not ' ' in gamestatus

# Function that checks if position to check
def check_availability(gamestatus, position):
    # True if position in gamestatus is empty
    # False ix box is already being used
    return gamestatus[position] == ' '


#########################################
# VARIABLES:                            #
#########################################
gamestatus = list()
finish = False
selection = ' '


#########################################
# MAIN CODE:                            #
#########################################

# Reset Game
gamestatus = reset_game()

while not finish:
    # Check if any Player already won or game tied
    if is_game_finished(gamestatus):
        while(selection != 'Y' and selection != 'N'):
            selection = raw_input('You want to play again? (Y/N): ')
            selection = selection.upper()

            if selection == 'Y': gamestatus = reset_game()
            elif  selection == 'N': finish = True
            else: print bcolors.BOLD,'Sorry but option typed is wrong!', bcolors.ENDC
        selection = ' '
    else:
        # Start Playing
        gamestatus = play(gamestatus)