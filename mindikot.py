# 4 players
# 2 teams, clockwise rotation 
# round winner plays the first card
# players must follow suit when possible,
# if not possible then fis chodo or play trump card to triumph other cards.
# each team should collect tricks,the team with the most tricks with card value of 10 wins the game.
# if both have equal 10s then the team with the most tricks win the game

import random

suits = ['Hearts', 'Spades', 'Diamonds', 'Clubs']
ranks = ['2','3','4','5','6','7','8','9','10','Jack','Queen', 'King', 'Ace']
values = {'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,'10':10,'Jack':11,'Queen':12,'King':13,'Ace':14}


class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
    
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    
    def __eq__(self, other):
        # This defines what happens when you use 'card1 > card2'
        return self.value == other.value
    
    def __gt__(self, other):
        return self.value > other.value
    
    def __le__(self, other):
        return self.value < other.value


deck = [Card(suit,rank) for suit in suits for rank in ranks]
random.shuffle(deck)

player1 = deck[:13]
player2 = deck[13:26]
player3 = deck[26:39]
player4 = deck[39:]

#player 1 throws a card and the suit of the card becomes the required suit for this round

#player 2 throws a card on same suit if possible, or if he doesnt have that suit he can throw the trump suit which makes him win, or any other suit which is basically useless.

#player 3 throws a card but is in the same team as player 1, so he plays accordingly.

#player 4 throws a card and is in the same team as player 2 and he plays accordingly.

#The highest value card wins the round,

#values are decided by Trump suit being on top, then the suit decided for that round .

#whoever wins the round starts the next round by throwing first

def user_turn(player_hand):
    print("\nyour hand:")
    for i,card in enumerate(player_hand):
        print(f"{i}: {card}")

        # player 1 turn
        # for i in range(0,len(player1)) :
        #     print(i, player1[i])

    while True:
        try:
            choice = int(input(f"Select a card to play (0-{len(player_hand)-1}): "))
            if 0 <= choice <len(player_hand):
                return player_hand.pop(choice)
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
            print(f"\nPLAYER {i+1} turn---------------")
            played_card = user_turn(player)
            middle_stack.append(played_card)
            print(f"\nPlayer {i+1} played : {played_card}")

    else:
        reordered = players[winner_index:] + players[:winner_index]

        for player in reordered:
            original_number = players.index(player) + 1  
            print(f"\nPLAYER {original_number} turn:")
            played_card = user_turn(player)
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


















# if middle_stack[i] > middle_stack[1]:
#         if middle_stack[0] > middle_stack[2]:
#             if middle_stack[0] > middle_stack[3]:
#                 print(middle_stack[0])
#                 winner_index = 0
#             else:
#                 print(middle_stack[3])
#                 winner_index = 3
#         elif middle_stack[2] > middle_stack[3]:
#             print(middle_stack[2])
#             winner_index = 2
#         else:
#             print(middle_stack[3])
#             winner_index = 3
#     elif middle_stack[1] > middle_stack[2]:
#         if middle_stack[1]> middle_stack[3]:
#             print(middle_stack[1])
#         else:
#             print(middle_stack[3])
#             winner_index = 3
#     elif middle_stack[2] > middle_stack[3]:
#         print(middle_stack[2])
#     else:
#         print(middle_stack[3])
#         winner_index = 3