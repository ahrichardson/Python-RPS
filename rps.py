from random import randint

win_list = [0, 0]
play_list = ["austin", "elissa"]

print "\n"*50
print """
     ------        Let's Playing Traditional Japanese JANKEN!     ------
    -------       Do you know? Choose rock, paper, or scissor!    -------
     ------                     Let's Trying!                     ------

"""

def win():
    print "\nYou played %s and the Japanese supercomputer played %s. You win!" % (play_list[0], play_list[1])
    win_list[0] += 1
    print_score()
    replay_check()

def lose():
    print "\n   You played %s and the Japanese supercomputer played %s. You lose!" % (play_list[0], play_list[1])
    win_list[1] += 1
    print_score()
    replay_check()

def tie():
    print "\nYou both played %s. You tied!" % play_list[0]
    print_score()
    replay_check()

def print_score():
    print """
    Player Wins: %s
    Computer Wins: %s
    """ % (win_list[0], win_list[1])

def replay_check():
    while True:
        replay = raw_input("Play again? (y/n)\n")
        if replay in ["yes", "YES", "Yes", "y", "Y"]:
            game()
        elif replay in ["no", "NO", "No", "N", "n"]:
            print "     FINAL SCORE:"
            print_score()
            quit(0)
        else:
            print "\nSorry, didn't quite catch that.\n"

def game():
    comp = randint(1,3)
    comp_def = {1: "rock", 2: "scissors", 3: "paper"}
    comp_play = comp_def[comp]
    while True:
        user = raw_input("\nRock, paper, or scissors?\n")
        if user in ["rock", "Rock", "ROCK", "R", "r"]:
            user_play = "rock"
            user = 1
            play_list[0] = user_play
            play_list[1] = comp_play
            if comp == 2:
                win()
            elif comp == 3:
                lose()
            else:
                tie()
        elif user in ["scissors", "Scissors", "SCISSORS", "S", "s"]:
            user_play = "scissors"
            user = 2
            play_list[0] = user_play
            play_list[1] = comp_play
            if comp == 3:
                win()
            elif comp == 1:
                lose()
            else:
                tie()
        elif user in ["paper", "Paper", "PAPER", "P", "p"]:
            user_play = "paper"
            user = 3
            play_list[0] = user_play
            play_list[1] = comp_play
            if comp == 1:
                win()
            elif comp == 2:
                lose()
            else:
                tie()
        else:
            print "\nSorry, didn't quite catch that.\n"
game()
