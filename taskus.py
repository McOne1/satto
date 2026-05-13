#1 dhanglabaji oop
#2 AI translate hindi to english.


#2 person - evenly divided cards- throw cards -
# a stack in middle 
#same number card equals the person last to put the card pick up the stack
# whoever has the most cards at the end wins 


# person_1 = 26 cards

# person_2 = 26 cards

# check = last_card + new_card

# mid_stack = mid_stack + new_card

# last_card = new_card 

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

    
# card1 = Card('Spades','4')
# card2 = Card('Clubs', '4')



# if card1==card2:
#     deck = []
#     deck.extend([card1, card2])
#     # print(deck[1])

deck = [Card(suit,rank) for suit in suits for rank in ranks]
random.shuffle(deck)

player_1 = deck[:26]
player_2 = deck[26:]
middle_stack = []



while player_1 and player_2:
    card_1 = player_1.pop(0)
    middle_stack.append(card_1)
    print("player 1:", card_1)

    if middle_stack[-2:-1] and card_1 == middle_stack[-2]:
        player_1.extend(middle_stack)
        middle_stack=[]
        print("Player 1 matched")

    card_2 = player_2.pop(0)
    middle_stack.append(card_2)
    print("player 2:",card_2)

    if middle_stack[-2:-1] and card_2 == middle_stack[-2]:
        player_2.extend(middle_stack)
        middle_stack=[]
        print("Player 2 matched")

    

print("player 1 len:",len(player_1))
print("player 2 len:",len(player_2))
















# while player_1 and player_2:
#     card_1 = player_1.pop(0)
#     print("card_1: ",card_1)
#     card_2 = player_2.pop(0)
#     print("card_2: ",card_2)
#     middle_stack.extend([card_1,card_2])
#     # print(middle_stack)

#     if card_2 == card_1:
#         player_2.extend(middle_stack)
#         print("player_2:",len(player_2))
#         middle_stack = []

#     else:
#         card_1 = player_1.pop(0)
#         print("card_1: ",card_1)
#         middle_stack.append(card_1)

#         if card_1 == card_2:    
#             print(card_1)
#             print(card_2)
#             player_1.extend(middle_stack)
#             print("player_1:",len(player_1))

#         elif card_1 != card_2:
#             card_2 = player_2.pop(0)
#             print("card_2: ",card_2)
#             middle_stack.append(card_2)
    
#         elif len(player_1) == 0 or len(player_2) == 0:
#             print("game over")
#             print("player 1",len(player_1))
#             print("player 2",len(player_2))