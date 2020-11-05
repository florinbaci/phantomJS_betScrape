# Rock, Paper, Scissors

import random, sys

# This variables will keep track of wins, losses and ties

wins = 0
losses = 0
ties = 0

while True:  # The main game loop.
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:  # The player input loop.
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit()  # Quit the program.
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break  # Break out of the player input loop.
        print('Type one of r, p, s, or q.')

    # Display what player choose:

    if playerMove == 'r':
        print('Rock vs...')
    elif playerMove == 'p':
        print('Paper vs...')
    elif playerMove == 's':
        print('Scissors vs...')

    # Dispaly what robot choose

    randomNumber = random.randint(1, 3)
    if randomNumber == 1:
        robotMove = 'r'
        print('Rock')
    elif randomNumber == 2:
        robotMove = 'p'
        print('Paper')
    elif randomNumber == 3:
        robotMove = 's'
        print('Scissors')

    # Dsiplay the score

    if playerMove == robotMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and robotMove == 'p':
        print('Robot have wins')
        losses = losses + 1
    elif playerMove == 'p' and robotMove == 'r':
        print('Player wins')
        wins = wins + 1
    elif playerMove == 's' and robotMove == 'r':
        print('Robot wins')
        losses = losses + 1
    elif playerMove == 'r' and robotMove == 's':
        print('Player wins')
        wins = wins + 1
    elif playerMove == 's' and robotMove == 'p':
        print('Player wins')
        wins = wins + 1
    elif playerMove == 'p' and robotMove == 's':
        print('Robot wins')
        losses = losses + 1








