from __future__ import annotations
import random

from enum import Enum
from functools import total_ordering
from typing import override


class Suit(Enum):
    # SUIT = (SYMBOL, LETTER)
    HEARTS = ("♥", "H")
    DIAMONDS = ("♦", "D")
    CLUBS = ("♣", "C")
    SPADES = ("♠", "S")

    def __init__(self, symbol: str, letter: str):
        self.symbol = symbol
        self.letter = letter


@total_ordering
class Rank(Enum):
    # RANK = (SYMBOL, ORDER)
    ACE = ("A", 14)
    KING = ("K", 13)
    QUEEN = ("Q", 12)
    JACK = ("J", 11)
    TEN = ("10", 10)
    NINE = ("9", 9)
    EIGHT = ("8", 8)
    SEVEN = ("7", 7)
    SIX = ("6", 6)
    FIVE = ("5", 5)
    FOUR = ("4", 4)
    THREE = ("3", 3)
    TWO = ("2", 2)

    def __init__(self, symbol: str, order: int):
        self.symbol = symbol
        self.order = order

    def __lt__(self, other: Rank) -> bool:
        return self.order < other.order


class Card:
    def __init__(self, rank: Rank, suit: Suit):
        self.rank: Rank = rank
        self.suit: Suit = suit

    @override
    def __repr__(self) -> str:
        return f"{self.rank.symbol}{self.suit.symbol}"

    def __lt__(self, other: Card) -> bool:
        if self.suit != other.suit:
            raise ValueError("Cannot compare cards of different suits.")
        return self.rank < other.rank

    @override
    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Card):
            return NotImplemented   # NOTE: RETURN an Exception, not raise.
        return self.rank == other.rank and self.suit == other.suit

    def __le__(self, other: Card) -> bool:
        return self < other or self == other

    # def __hash__(self) -> int:
    #     return hash((self.rank, self.suit))


class Deck[CardT: Card](list[CardT]):
    @override
    def __repr__(self) -> str:
        return f"Deck(cards={list.__repr__(self)})"

    def shuffle(self) -> None:
        random.shuffle(self)

    @classmethod
    def standard_deck(cls) -> Deck[Card]:
        return cls(Card(rank, suit) for rank in Rank for suit in Suit)