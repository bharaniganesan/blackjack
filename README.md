# Blackjack game
This is a Python implementation of a blackjack game, which is the 2nd milestone project in the Udemy course: Complete Python Bootcamp. This is a simplified version where more complex strategies like splitting the hand or insurance are
not implemented.

## High level code structure
The code is structured in four files - dealer.py, player.py, cardDeck.py and blackjack_milestone2_v3.py

### abstractEntity.py
Abstract entity class that provides the attributes and methods common to the Dealer and the Player.
Dealer and Player classes will inherit the AbstractEntity class.

### dealer.py
Dealer class that inherits the AbstractEntity class and also provides additional methods that are needed by the Dealer.

### player.py
Player class that inherits the AbstractEntity class and also provides additional methods that are needed by the Player such as making bets and displaying the hand.

### cardDeck.py
Class for holding the card deck. The deck itself and the card values will be stored as class attributes.

### blackjack_milestone2_v3.py
This is the entry point of the Blackjack program. This script controls the game play and has the logic for dealing cards, checking various states of the game such as bust or blackjack. It also keeps track of the winnings of the player. 

## Steps to running this code locally
Download the files in this repository. Execute the following code in the command prompt at the location where you saved these files

```python blackjack_milestone2_v3.py```

## Enhancement ideas
1. The code can be enhanced to handle more complex strategies such as splits and insurance. 
2. Refactor some of the utility functions in blackjack_milestone2_v3.py and move it out to a Utility class.
