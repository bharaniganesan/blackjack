#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:28:44 2019

@author: Bharani Ganesan


"""
from abstractEntity import AbstractEntity

#Player class
class Player(AbstractEntity):
    
    def __init__(self, card_value_dnry):
        AbstractEntity.__init__(self, card_value_dnry)
        print("Player created.")
        
    def make_bet(self, BET_MADE):
        if self.bank_roll >= BET_MADE:
            self.bank_roll = self.bank_roll -  BET_MADE
            print(f"Bet made. Your new bank roll is ${self.bank_roll}.\n")
        else:
            print("Sorry. You don't have enough to make a bet. You cannot play anymore!\n")
            return False
    
    def cards_received(self, card_received):
        if card_received != None:
            self.cards_held.append(card_received)
            if card_received == "A":
                while True:
                    value_a = int(input("What would you like the A to be valued as (1 or 11)?: \n"))
                    if value_a == 1 or value_a == 11:
                        self.total_card_value(value_a)
                        break
                    else:
                        print("Invalid entry. Please enter 1 or 11.\n")
            else:
                self.total_card_value(self.card_value_dnry[card_received])
    
    def show_all_cards(self):
        print(f"Your cards received are {self.cards_held} with a value of {self.card_value}\n")