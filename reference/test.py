from mindikot import deal
from core.cards import Card,Deck, Rank, Suit

from player import Player

deck = Deck([Card(suit,rank) for suit in Suit for rank in Rank])

deck.shuffle()

# player1 = Player(deck.cards[0:13], "Player 1")
# player2 = Player(deck.cards[13:26], "Player 2")
# player3 = Player(deck.cards[26:39], "Player 3")
# player4 = Player(deck.cards[39:], "Player 4")


player1, player2,player3, player4 = deal(deck,4)



print(player1)
print(player2)
print(player3)
print(player4)