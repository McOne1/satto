from game import Game
from player import Player
from core.cards import Deck 

player_1: Player = Player("Rakesh")
player_2: Player = Player("Mahesh")
player_3: Player = Player("Suresh")
player_4: Player = Player("Dharmesh")
players = [player_1,player_2,player_3,player_4]

game = Game(Deck.standard_deck(), players)

game.deal_cards(True)

# game.hide_trump_from_lead_player()

lead_player_index = 0

for i in range(13):   
    if game.trump_suit == None:
        is_reveal_trump = False
    else:
        is_reveal_trump = True

    winner = game.play_trick(lead_player_index,is_reveal_trump)
    print(f"{winner.name} won the trick")
    lead_player_index = players.index(winner)

game.most_tricks_won()

