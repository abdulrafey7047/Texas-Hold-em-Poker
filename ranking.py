from typing import List
from collections import Counter

from card import Card
from hand import Hand
from utils import number_map

class HandRanking:

    @classmethod
    def _most_same_suit_cards(cls, hand: Hand) -> List[Card]:

        card_suits_in_hand = [ card.suit for card in hand ]
        suit_occurances = Counter(card_suits_in_hand)
        most_occured_suit = suit_occurances.most_common()[0][0]
        most_same_suit_cards = [ card for card in hand if card.suit == most_occured_suit ]

        return most_same_suit_cards

    @classmethod
    def _in_sequence(cls, cards: List[Card], n: int) -> bool:

        sotrted_card_numbers_in_hand = sorted(list(set([ card.number for card in cards ])))
        consecutive_count = 1
        for i in range(len(sotrted_card_numbers_in_hand) - 1):
            if sotrted_card_numbers_in_hand[i+1] - sotrted_card_numbers_in_hand[i] == 1:
                consecutive_count += 1
            else:
                consecutive_count = 1
            
            if consecutive_count == n:
                return True
        return False

    @classmethod
    def _has_highest_cards(cls, cards: List[Card], n: int) -> bool:
        
        card_numbers_in_hand = [ card.number for card in cards ]
        highest_cards_possible = sorted(number_map.values(), reverse=True)[:n]
        highest_cards_in_hand =  sorted(card_numbers_in_hand, reverse=True)[:n]

        return set(highest_cards_possible) == set(highest_cards_in_hand)

    def _is_royal_flush(cls, hand: Hand) -> bool:

        same_suit_cards = cls._most_same_suit_cards(hand)
        if (len(same_suit_cards) >= 5) and cls._in_sequence(same_suit_cards, n=5) and cls._has_highest_cards(same_suit_cards, n=5):
            return True

        return False

    @classmethod
    def _is_straight_flush(cls, hand: Hand) -> bool:

        same_suit_cards = cls._most_same_suit_cards(hand)
        if (len(same_suit_cards) >= 5) and cls._in_sequence(same_suit_cards, n=5):
            return True

        return False

        

    @classmethod
    def rank(cls, hand: Hand) -> int:

        card_numbers_in_hand = [ card.number for card in hand ]
        number_occurances = Counter(card_numbers_in_hand)

        # Royal Flush
        if cls._is_royal_flush(cls, hand):
            return 10
        # Straight Flush
        elif cls._is_straight_flush(hand):
            return 9
        # Four of a Kind
        elif 4 in number_occurances.values():
            return 8
        # Full House
        elif (3 in number_occurances.values()) and (2 in number_occurances.values()):
            return 7
        # Flush
        elif len(cls._most_same_suit_cards(hand)) >= 5:
            return 6
        # Straight
        elif  cls._in_sequence(hand, n=5):
            return 5
        # Three of a Kind
        elif 3 in number_occurances.values():
            return 4
        # Two Pairs
        elif list(number_occurances.values()).count(2) == 2:
            return 3
        # One Pair
        elif 2 in number_occurances.values():
            return 2
        # High Card
        else:
            return 1
