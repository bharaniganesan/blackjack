#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 29 14:22:43 2019

@author: Bharani Ganesan

Dealer class that inherits the AbstractEntity class and also provides additional methods
that are needed by the Dealer.
"""

from abstractEntity import AbstractEntity

#Dealer class
class Dealer(AbstractEntity):
    
    def __init__(self, cardValueDnry):
        AbstractEntity.__init__(self, cardValueDnry)
        print("Dealer Created.")
    
    def show_first_card(self):
        print(f"Dealer's first open card is {self.cards_held[0]}.")
    
    def show_all_cards(self):
        print(f"Dealer cards held are: {self.cards_held} with a value of {self.card_value}.")