import random

from itertools import cycle

from games.mindikot.player import Player, Trick
from core.cards import Card, Deck, Rank, Suit


NUM_PLAYERS = 4


class Game:
    def __init__(self, deck: Deck, players: list[Player]) -> None:
        if len(players) != NUM_PLAYERS:
            raise ValueError(f"Expected {NUM_PLAYERS} players, got {len(players)}.")
        self.deck: Deck = deck
        self.players: list[Player] = players
        self.hidden_trump_card: Card | None = None
        self.trump_suit: Suit | None = None

    def deal_cards(self, shuffle: bool = True) -> None:
        """Shuffle the deck and then equally deal the cards to the players."""
        if shuffle:
            self.deck.shuffle()
        for i, player in enumerate(self.players):
            player.hand = self.deck[i :: len(self.players)]

    # # Phase 1
    def hide_trump_from_lead_player(self) -> None:
        hidden_card: Card = random.choice(self.players[0].hand)
        self.players[0].hand.remove(hidden_card)
        self.hidden_trump_card = hidden_card

    def reveal_trump_card(self) -> None:
        self.trump_suit = self.hidden_trump_card.suit
        self.players[0].hand.append(self.hidden_trump_card)

    @staticmethod
    def _determine_winning_card(trick: Trick) -> Card:
        winning_card: Card = trick[0]
        led_suit: Suit = trick[0].suit
        for card in trick:
            if card.suit == led_suit and winning_card < card:
                winning_card = card
        return winning_card
    
    def _determine_winning_card_after_trump_reveal(trick: Trick, trump_suit: Suit) -> Card:
        winning_card: Card = trick[0]
        led_suit: Suit =  trick[0].suit

        if trick[0].suit == trump_suit:
            for card in trick:
                if card.suit == led_suit and winning_card < card:
                    winning_card = card
            return winning_card
        else:
            for card in trick:
                if card.suit == trump_suit and winning_card.suit != trump_suit:
                    winning_card = card
                elif card.suit == trump_suit and winning_card.suit == trump_suit and winning_card < card:
                    winning_card = card
                  


    @staticmethod
    def player_input_prompt(player: Player, led_suit: Suit | None, trick: Trick) -> None:
        print(f"\n{player.name}'s Turn...")
        print(f"Led Suit: {led_suit if led_suit else '-'}, Trick so far: {trick}")
        print(f"{player.name}'s Hand: ")
        for i, card in enumerate(player.hand):
            print(f" [{i}] {card}", end="")
        print()


    def most_tricks_won(self):
        team_1_tricks = self.players[0].won_tricks + self.players[2].won_tricks
        team_2_tricks = self.players[1].won_tricks + self.players[3].won_tricks
        team_1_tricks_amount=  len(team_1_tricks)
        team_2_tricks_amount=  len(team_2_tricks)
        mindi_counter_team2 = 0
        mindi_counter_team1 = 0 

        for trick in team_1_tricks:
            for card in trick:
                if card.rank == Rank.TEN:
                    mindi_counter_team1 += 1

        for trick in team_2_tricks:
            for card in trick:
                if card.rank == Rank.TEN:
                    mindi_counter_team2 += 1

        if mindi_counter_team1 > mindi_counter_team2:
            print("team 1 wins")
        elif mindi_counter_team1 < mindi_counter_team2:
            print("team 2 wins")
        else:
            if team_1_tricks_amount > team_2_tricks_amount:
                print("team 1 wins")
            else:
                print("teams 2 wins")
        
        

    # Phase 2
    def play_trick(self, lead_player_index, is_trump_reveal:bool) -> Player:

        ordered_players = self.players[lead_player_index:] + self.players[:lead_player_index]

        trick: Trick = []   # table par patta
        for player in ordered_players:
            led_suit = trick[0].suit if trick else None
            while True:
                try:
                    self.player_input_prompt(
                        player=player,
                        led_suit=led_suit,
                        trick=trick
                    )
                    print("",end="",flush=True)
                    player_selected_idx: int = int(input("Enter index of card you want to play: "))
                    player_selected_card: Card = player.hand[player_selected_idx]
            


                    trick.append(player.play_card(player_selected_card, led_suit))
                    break                
                except ValueError as ve:
                    print("!!!!!!!!!Error:",ve)
                    continue
        # dertimine trick winner here and award it.
        if is_trump_reveal == False:
            winning_card = self._determine_winning_card(trick)
        else:
            winning_card = self._determine_winning_card_after_trump_reveal(trick, self.trump_suit)
        winner: Player = ordered_players[trick.index(winning_card)]

        winner.collect_winning_trick(trick)
        return winner
    

