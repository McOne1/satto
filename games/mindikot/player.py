from typing import override
from core.cards import Card, Suit


Hand = list[Card]
Trick = list[Card]

class Player:
    def __init__(self, name: str, hand: Hand = []) -> None:
        self.name: str = name
        self.hand: Hand = hand
        self.won_tricks: list[Trick] = []   # Haath

    def __repr__(self) -> str:
        return f"Player(name={self.name}, hand={self.hand})"

    def play_card(self, card: Card, led_suit: Suit) -> Card:
        if card.suit != led_suit and led_suit in [hcard.suit for hcard in self.hand]:
            raise ValueError("Player must follow Suit!!!!!!!")
        try:         
            self.hand.remove(card)
            return card
        except ValueError:
            raise ValueError(f"{self} does not have the card {card} in hand.")

    def collect_winning_trick(self, won_trick: Trick) -> None:
        self.won_tricks.append(won_trick)