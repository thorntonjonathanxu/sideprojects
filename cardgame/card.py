
from dataclasses import dataclass
import pygame
import random

@dataclass
class Card():
    suit : str
    name: str

    def __init__(self, suit : str, name:str) -> None:
        self.suit = suit
        self.name = name
        pass

    def __repr__(self) -> str:
        return f"{self.suit} {self.name}"

class Deck():
    def __init__(self) -> None:
        self.cards_list = []
    
    def __repr__(self) -> str:
        return f"Deck of {len(self.cards_list)}, Cards: {self.cards_list}"

    def addcard(self, card:Card):
        """function adds a card to the deck"""
        self.cards_list.append(card)

    def removecard(self, card:Card):
        """removes a selected card from the deck"""
        if self.isempty():
            print("Can't remove card deck is empty")
            return 
        if card not in self.cards_list:
            print("Card doesn't exist")
            return
        self.cards_list.pop(card)

    def dealcard(self):
        """removes the next card in the deck"""
        return self.cards_list.pop()

    def shuffle(self):
        """shuffles the deck of cards"""
        random.shuffle(self.cards_list)

    def emptydeck(self):
        """clears out the deck"""
        self.cards_list = []
    
    def isempty(self):
        """helper function to check if deck is empty"""
        return len(self.cards_list) == 0
        
class DeckConfig():
    def __init__(self, deck : Deck, config : str = None) -> None:
        self.deck = deck
        pass

    def generatedeck(self,suits:list,numbers:list):
        [self.deck.addcard(Card(suit,num)) for suit in suits for num in numbers]
        
    def standard_deck(self):
        suits = ["Spade", "Club", "Diamond", "Heart"]
        numbers = ["1","2","3","4","5","6","7","8","9","10","J","Q","K"]
        self.generatedeck(suits,numbers)
        return self.deck

    def euchre_deck(self):
        suits = ["Spade", "Club", "Diamond", "Heart"]
        numbers = ["9","10","J","Q","K"]
        self.generatedeck(suits,numbers)
        return self.deck

class Player():
    def __init__(self, name: str) -> None:
        self.name = name
        self.hand = []

    def __repr__(self) -> None:
        return f"Player: {self.name}, Cards : {len(self.hand)}, Hand: {self.hand}"

    def draw(self, card: Card ):
        """add a selected card to the players hand"""
        self.hand.append(card)
    
    def play(self, card: Card):
        """remove a selected card from the players hand"""
        if self.isempty(): 
            print("Hand is empty can't play any cards")
            return
        self.hand.pop(card)

    def isempty(self):
        """helper function to check if hand is empty"""
        return self.hand == 0 

class Game():
    def __init__(self, players:list[Player], mode:enumerate) -> None:
        self.players = players
        self.mode = mode
    
    
        

def main():
    mydeck = Deck()
    mydeck = DeckConfig(mydeck).euchre_deck()
    
    mydeck.shuffle()

    p1 = Player("Jon")
    p2 = Player("Ton")
    p3 = Player("Fon")
    p4 = Player("Bon")
    
    players = [p1,p2,p3,p4]

    x = 0
    full_list = mydeck.cards_list.copy()
    for i in full_list:
        players[x].draw(mydeck.dealcard())
        x += 1
        if x > 3:
            x = 0
        

    for player in players:
        print(player)

if __name__ == "__main__":
    main()