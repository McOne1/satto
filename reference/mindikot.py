# 4 players
# 2 teams, clockwise rotation 
# round winner plays the first card
# players must follow suit when possible,
# if not possible then fis chodo or play trump card to triumph other cards.
# each team should collect tricks,the team with the most tricks with card value of 10 wins the game.
# if both have equal 10s then the team with the most tricks win the game

from core.cards import Card,Deck, Rank, Suit
from games.mindikot.player import Player

deck = Deck([Card(suit,rank) for suit in Suit for rank in Rank])

deck.shuffle()

def deal(deck, num_players:int) -> list[list[Card]]:
    cards_per_player = len(deck) // num_players

    return [deck[i*cards_per_player:(i+1)*cards_per_player]
            for i in range(num_players)
    ]

playerss = []
for i, one_deal in enumerate(deal(deck,4)):
    playerss.append( Player(one_deal, f"Player{i+1}"))

for i, player in enumerate(playerss):
     locals()[f"player{i+1}"] = player

# print(player1)
# player1 = Player(deck.cards[0:13], "Player 1")
# player2 = Player(deck.cards[13:26], "Player 2")
# player3 = Player(deck.cards[26:39], "Player 3")
# player4 = Player(deck.cards[39:], "Player 4")

#player 1 throws a card and the suit of the card becomes the required suit for this round

#player 2 throws a card on same suit if possible, or if he doesnt have that suit he can throw the trump suit which makes him win, or any other suit which is basically useless.

#player 3 throws a card but is in the same team as player 1, so he plays accordingly.

#player 4 throws a card and is in the same team as player 2 and he plays accordingly.

#The highest value card wins the round,

#values are decided by Trump suit being on top, then the suit decided for that round .

#whoever wins the round starts the next round by throwing first

def user_turn(player: Player, required_suit = None):
    print("\nyour hand:")
    for i,card in enumerate(player.cards):
        print(f"{i}: {card}")

    has_required_suit = any(card.suit == required_suit for card in player.cards)

    while True:
        try:
            choice = int(input(f"Select a card to play (0-{len(player.cards)-1}): "))
            if 0 <= choice <len(player.cards):
                selected_card = player.cards[choice]
                if required_suit and has_required_suit and selected_card.suit != required_suit:
                    print(f"You must play a {required_suit.value[0]} card!")
                    # no return → loops back and asks again ✅
                else:
                    return player.cards.pop(choice)
            else:
                print("invalid index")
        except ValueError:
            print("please enter a valid number")


winner_index = -1 
players= [player1,player2, player3,player4]
mindi_counter_team1 = 0
hand_counter_team1 = 0

mindi_counter_team2 = 0
hand_counter_team2 = 0

while player1 and player2 and player3 and player4:
    
    middle_stack = []

    if winner_index == -1:
        reordered= [player1,player2, player3,player4]

        for i,player in enumerate(players):
            if len(middle_stack)==0:
                print(f"\nPLAYER {i+1} turn---------------++")
                played_card = user_turn(player)
                middle_stack.append(played_card)
                print(f"\nPlayer {i+1} played : {played_card}")
                required_suit= played_card.suit

            else:
                print(f"\nPLAYER {i+1} turn---------------!!")
                played_card = user_turn(player, required_suit)
                middle_stack.append(played_card)
                print(f"\nPlayer {i+1} played : {played_card}")

    else:
        reordered = players[winner_index:] + players[:winner_index]

        for  i,player in enumerate(reordered):
            if len(middle_stack)==0:
                original_number = players.index(player) + 1  
                print(f"\nPLAYER {original_number} turn:")
                played_card = user_turn(player)
                middle_stack.append(played_card)
                print(f"\nPlayer {original_number} played: {played_card}")
                required_suit= played_card.suit
            else:
                original_number = players.index(player) + 1  
                print(f"\nPLAYER {original_number} turn:")
                played_card = user_turn(player, required_suit)
                middle_stack.append(played_card)
                print(f"\nPlayer {original_number} played: {played_card}")

    print("\nMiddle Stack:")
    for i in middle_stack:
        print(i)

    original_number = players.index(player) + 1

    if middle_stack[0] > middle_stack[1]:
        if middle_stack[0] > middle_stack[2]:
            if middle_stack[0] > middle_stack[3]:
                print("winner:",middle_stack[0])
                winner_index = players.index(reordered[0])
                print("player:",winner_index)
            else:
                print(middle_stack[3])
                winner_index = players.index(reordered[3])
                print("player:",winner_index)
        elif middle_stack[2] > middle_stack[3]:
            print(middle_stack[2])
            winner_index = players.index(reordered[2])
        else:
            print(middle_stack[3])
            winner_index = players.index(reordered[3])
    elif middle_stack[1] > middle_stack[2]:
        if middle_stack[1]> middle_stack[3]:
            print(middle_stack[1])
            winner_index = players.index(reordered[1])
        else:
            print(middle_stack[3])
            winner_index = players.index(reordered[3])
    elif middle_stack[2] > middle_stack[3]:
        print(middle_stack[2])
        winner_index = players.index(reordered[2])
    else:
        print(middle_stack[3])
        winner_index = players.index(reordered[3])

    if winner_index == 0 or winner_index == 2:
        hand_counter_team1= hand_counter_team1+1
        print("team1:",hand_counter_team1)
        print("team2:",hand_counter_team2)
    else:
        hand_counter_team2 = hand_counter_team2+1
        print("team1:",hand_counter_team1)
        print("team2:",hand_counter_team2)