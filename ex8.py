# Make a two-player Rock-Paper-Scissors game. 

# Hint: 
#   Ask for player plays (using input)
#   compare them
#   print out a message of congratulations to the winner
#   ask if the players want to start a new game

# Remember the rules:
#   Rock beats scissors
#   Scissors beats paper
#   Paper beats rock

new_game = True

while new_game != False:

    print("WELCOME TO ROCK-PAPER-SCISSORS")
    print("==============================")

    player_one = input("Please enter your name, Player 1 >>> ")
    player_two = input("Please enter your name, Player 2 >>> ")

    player_one_answer = input("%s, Please choose Rock, Paper, or Scissors >>> " % player_one).upper()
    player_two_answer = input("%s, Please choose Rock, Paper, or Scissors >>> " % player_two).upper()

    if player_one_answer and player_two_answer == 'ROCK' or 'PAPER' or 'SCISSORS':        
        if player_one_answer == player_two_answer:
            print("It's a tie!")
        elif ((player_one_answer == 'ROCK') & (player_two_answer == 'SCISSORS')) | ((player_one_answer == 'PAPER') & (player_two_answer == 'ROCK')) | ((player_one_answer == 'SCISSORS') & (player_two_answer == 'PAPER')):
            print('Player 1 wins!')
        else:
            print('Player 2 wins!')
    else:
        print("You did not enter rock, paper or scissors")

    new = input ("Do you want to play again? Y or N >>> ")

    if new == 'Y':
        continue
    else:
        print("Thanks for playing!")
        new_game = False