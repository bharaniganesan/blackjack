#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 22 20:35:33 2019

@author: bharani_preethi

This is an implementation of a blackjack game, which is the 2nd milestone
project in the Udemy course: Complete Python Bootcamp. This is a simplified
version where more complex strategies like splitting the hand or insurance are
not implemented.
"""
#Import the required classes
from dealer import Dealer
from player import Player
from cardDeck import CardDeck

#Import random module from numpy to draw cards randomly
from numpy import random

BET_SIZE = 5 #bet size for each game

def initial_deal():
    """
    Deals initial cards for player and dealer. Player's both cards are
    shown, while only one card for dealer is shown.
    """
    for i in range(0, 2):
        player1.cards_received(CardDeck.cards[random.randint(1, 12)])

    for i in range(0, 2):
        dealer1.cards_received(CardDeck.cards[random.randint(1, 12)])

#Pick a card at random if requested by player
def deal_card_to_player():
    """
    Deals cards to player and checks if player wants to hit or stand
    """
    while True:
        deal_card = input("Would you like to hit? (Y/N):")
        if deal_card.upper() == "Y":
            return CardDeck.cards[random.randint(1, 13)]
        if deal_card.upper() == "N":
            return None
        print("Invalid entry. Please enter Y or N.")

def check_if_bust(entity):
    """
    Check if the player or dealer card total is greater than 21
    """
    return entity.card_value > 21

def check_if_blackjack(entity):
    """
    Check if the player or dealer card total is 21
    """
    return entity.card_value == 21

#------------------------ Instantiate classes for player and dealer ----------------------------
print('Welcome to Black Jack! \n The Player starts with a bankroll of $100.\
      \n The bet size for each game is $5.\n')

player1 = Player(CardDeck.card_value_dnry)
dealer1 = Dealer(CardDeck.card_value_dnry)

while True:
    PLAY_GAME_AGAIN = input("Would you like to play? (Y/N): ")

    if PLAY_GAME_AGAIN.upper() == "Y" or PLAY_GAME_AGAIN.upper() == "N":
        break
    else:
        print("Invalid entry. Please enter Y or N.")

while PLAY_GAME_AGAIN.upper() == "Y":
    player1.cards_held = []
    dealer1.cards_held = []
    player1.card_value = 0
    dealer1.card_value = 0

    player1.make_bet(BET_SIZE)

    initial_deal() #Deal the first pair of cards for player and dealer

    dealer1.show_first_card() #Show the dealer's first card

    player1.show_all_cards() #Show the player's first cards

    #------------------------ Main loop of the game ------------------------
    #Player's loop
    while True:
        #Check if bust
        if check_if_bust(player1):
            print(f"Player bust!!! Your total card value is {player1.card_value}.")
            PLAY_CONTINUE = "N"
            break

        #Otherwise, check if player has won
        elif check_if_blackjack(player1):
            print(f"Blackjack!! Player wins!!! Your total card value is {player1.card_value}.")
            player1.add_to_bank_roll(BET_SIZE * 2)
            PLAY_CONTINUE = "N"
            break

        #Else check if they want to hit or stand
        else:
            cardDealt = deal_card_to_player()
            if cardDealt != None:
                player1.cards_received(cardDealt)
                player1.show_all_cards()
            else:
                PLAY_CONTINUE = "Y"
                break

    #Dealer loop
        #Open both cards
    if PLAY_CONTINUE == "Y":
        dealer1.show_all_cards()

        while True:
            #Keep hitting till > player value and <= 21, bust leads to loss
            if dealer1.card_value <= player1.card_value:
                dealer1.cards_received(CardDeck.cards[random.randint(1, 13)])
                dealer1.show_all_cards()

                #Check if bust
                if check_if_bust(dealer1):
                    print(f"Dealer bust!!! You win!!! Dealer's total card\
                                          value is {dealer1.card_value}.\n")
                    player1.add_to_bank_roll(BET_SIZE * 2)
                    break

                if check_if_blackjack(dealer1):
                    print(f"Blackjack!! Dealer wins!!! Dealer's total card\
                                          value is {dealer1.card_value}.\n")
                    break

            elif check_if_bust(dealer1):
                print(f"Dealer bust!!! You win!!! Dealer's total card value\
                                                  is {dealer1.card_value}.\n")
                player1.add_to_bank_roll(BET_SIZE * 2)
                break

            elif check_if_blackjack(dealer1):
                print(f"Blackjack!! Dealer wins!!! Dealer's total card value\
                                                  is {dealer1.card_value}.\n")
                break

            else:
                print(f"Dealer wins!!! Dealer's score is {dealer1.card_value}. \n")
                break

    print("Thank you for playing!\n")

    while True:
        PLAY_GAME_AGAIN = input("Would you like to play again? (Y/N): ")

        if PLAY_GAME_AGAIN.upper() == "Y" or PLAY_GAME_AGAIN.upper() == "N":
            break
        else:
            print("Invalid entry. Please enter Y or N.")
