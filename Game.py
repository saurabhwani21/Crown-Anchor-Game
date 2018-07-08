# Author: Saurabh A. Wani
# Crown and Anchor Game

import random
import sys

class Player:
    # Stores the player number
    playerNumber = 0
    # Store the player credit
    credit = 10
    # Stores the tokens on which the player placed bet on a given round
    betToken = []
    # Stores the bet amount placed by player for a given round
    betAmount = 0
    # Keeps track of round number for a player
    round = 0
    # Stores players winnings for all rounds
    gameDetails = {}


class Game:
    
    tokens = {1: "Hearts", 2: "Spades", 3: "Diamond", 4: "Clubs", 5: "Crown", 6: "Anchors"}
    listOfPlayers = []

    def __init__(self):
        print("Crown and Anchor \nWelcome!")
        # Total number of players who will be playing the game
        numOfPlayers = int(input("Enter the total number of players:"))
        for i in range (0,numOfPlayers):
            self.listOfPlayers.append(Player())

    def play(self, player):
        while player.credit > 0:
            player.round += 1
            player.betToken = []
            player.betAmount = 0
            winnings = 0
            print("Round ", player.round)
            # Display current credit
            print("Your current credit : ", player.credit)
            # Check for number of bets to be placed for a round
            numOfBets = int(input("Enter the number of bets you wish to place for this round (0-3)"))
            # If player wishes to skip this round
            if numOfBets == 0:
                print("Skipping this round for player ",player.playerNumber)
                continue
            # If invalid input then exit
            elif numOfBets not in [1, 2, 3]:
                print("Invalid input!")
                break
            #  Take user defined bet information
            for x in range(0, numOfBets):
                print("1: Hearts | 2: Spades | 3: Diamonds | 4: Club | 5: Crown | 6: Anchor | 0: Quit")
                betT = int(input("Enter the token you wish to place bet on [1,2,3,4,5,6] : "))
                # If user wants to quit
                if betT == 0:
                    print("Terminating!")
                    sys.exit()
                else:
                    player.betToken.append(betT)
                betA = int(input("Enter your bet amount [1,2,5,10] : "))
                if betA in [1, 2, 5, 10] and betA <= player.credit:
                    player.betAmount += betA
                else:
                    print("Invalid bet! Try again")
                    break
            # Generate random tokens
            print("Spinning the wheel.")
            token1 = random.randint(1, 6)
            token2 = random.randint(1, 6)
            token3 = random.randint(1, 6)
            print("Tokens generated : ", self.tokens[token1], " ", self.tokens[token2], " ", self.tokens[token3])
            # Check for winnings
            if token1 == token2 == token3:
                if token1 in player.betToken:
                    winnings += 3
                    print("Winner on ", self.tokens[token1])
            else:
                if (token1 in player.betToken):
                    winnings += 1
                if (token2 in player.betToken):
                    winnings += 1
                if (token3 in player.betToken):
                    winnings += 1
            # Updates player's credit
            if winnings == 0:
                player.credit -= player.betAmount
            else:
                player.credit = player.credit + (player.betAmount * winnings)
                print("Your current round winning: ", (player.betAmount * winnings))
                print("Your new credit is : ",player.credit)
            if (player.credit <= 0):
                print("Game over! Insufficient balance for further rounds.")
            player.gameDetails[player.round] = player.betAmount * winnings

    

if __name__ == '__main__':
    game = Game()
    for person in game.listOfPlayers:
        game.play(person)



