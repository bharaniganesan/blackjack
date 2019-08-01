#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:18:21 2019

@author: Bharani Ganesan

Abstract entity class that provides the attributes and methods common to the Dealer and the Player.
Dealer and Player classes will inherit the AbstractEntity class.
"""

#Dealer class
class AbstractEntity():
    
    def __init__(self, card_value_dnry, bank_roll = 100, cards_held = [], card_value = 0):
        self.bank_roll = bank_roll
        self.cards_held = cards_held
        self.card_value = 0
        self.card_value_dnry = card_value_dnry
        
    def add_to_bank_roll(self, winnings):
        self.bank_roll = self.bank_roll + winnings
        print(f"Player's bank_roll is now ${self.bank_roll}.")
        
    def cards_received(self, card_received):
        self.cards_held.append(card_received)
        self.total_card_value(self.card_value_dnry[card_received])
        
    def total_card_value(self, card_value):
        self.card_value += card_value