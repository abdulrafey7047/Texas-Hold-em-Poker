from typing import List
from collections import Counter

from card import Card
from hand import Hand
from utils import number_map


class HandRanker:
    """Ranks a hand of playing cards based on poker hand rankings."""

    @classmethod
    def _most_same_suit_cards(cls, hand: Hand) -> List[Card]:
        """
        Get the cards with the most occurrences of the same suit in a hand.

        Args:
            hand (Hand): The Hand object representing the hand of cards.

        Returns:
            List[Card]: The list of Card objects with the most occurrences of the same suit.
        """
        card_suits_in_hand = [card.suit for card in hand]
        suit_occurrences = Counter(card_suits_in_hand)
        most_occurred_suit = suit_occurrences.most_common()[0][0]
        most_same_suit_cards = [card for card in hand if card.suit == most_occurred_suit]

        return most_same_suit_cards

    @classmethod
    def _in_sequence(cls, cards: List[Card], n: int) -> bool:
        """
        Check if a list of cards has a sequence of n consecutive numbers.

        Args:
            cards (List[Card]): The list of Card objects representing the cards to check.
            n (int): The number of consecutive cards required.

        Returns:
            bool: True if the list of cards has a sequence of n consecutive numbers, False otherwise.
        """
        sorted_card_numbers_in_hand = sorted(list(set([card.number for card in cards])))
        consecutive_count = 1
        for i in range(len(sorted_card_numbers_in_hand) - 1):
            if sorted_card_numbers_in_hand[i + 1] - sorted_card_numbers_in_hand[i] == 1:
                consecutive_count += 1
            else:
                consecutive_count = 1

            if consecutive_count == n:
                return True
        return False

    @classmethod
    def _has_highest_possible_cards(cls, cards: List[Card], n: int) -> bool:
        """
        Check if a list of cards has the highest n cards.

        Args:
            cards (List[Card]): The list of Card objects representing the cards to check.
            n (int): The number of highest cards required.

        Returns:
            bool: True if the list of cards has the highest n cards, False otherwise.
        """
        card_numbers_in_hand = [card.number for card in cards]
        highest_cards_possible = sorted(number_map.values(), reverse=True)[:n]
        highest_cards_in_hand = sorted(card_numbers_in_hand, reverse=True)[:n]

        return set(highest_cards_possible) == set(highest_cards_in_hand)

    @classmethod
    def _is_royal_flush(cls, hand: Hand) -> bool:
        """
        Check if a hand has a Royal Flush.

        Args:
            hand (Hand): The Hand object representing the hand of cards.

        Returns:
            bool: True if the hand has a Royal Flush, False otherwise.
        """
        same_suit_cards = cls._most_same_suit_cards(hand)
        if len(same_suit_cards) >= 5 and cls._in_sequence(same_suit_cards, n=5) and cls._has_highest_possible_cards(same_suit_cards, n=5):
            return True
        return False

    @classmethod
    def _is_straight_flush(cls, hand: Hand) -> bool:
        """
        Check if a hand has a Straight Flush.

        Args:
            hand (Hand): The Hand object representing the hand of cards.

        Returns:
            bool: True if the hand has a Straight Flush, False otherwise.
        """
        same_suit_cards = cls._most_same_suit_cards(hand)
        if len(same_suit_cards) >= 5 and cls._in_sequence(same_suit_cards, n=5):
            return True
        return False

    @classmethod
    def rank(cls, hand: Hand) -> int:
        """
        Rank a hand of cards based on poker hand rankings.

        Args:
            hand (Hand): The Hand object representing the hand of cards.

        Returns:
            int: The rank of the hand. The higher the rank, the better the hand.
        """
        card_numbers_in_hand = [card.number for card in hand]
        number_occurrences = Counter(card_numbers_in_hand)

        # Royal Flush
        if cls._is_royal_flush(hand):
            return 10
        # Straight Flush
        elif cls._is_straight_flush(hand):
            return 9
        # Four of a Kind
        elif any(occurrence >= 4 for occurrence in number_occurrences.values()):
            return 8
        # Full House
        elif any(occurrence >= 3 for occurrence in number_occurrences.values()) and any(
            occurrence >= 2 for occurrence in sorted(number_occurrences.values())[:-1]
        ):
            return 7
        # Flush
        elif len(cls._most_same_suit_cards(hand)) >= 5:
            return 6
        # Straight
        elif cls._in_sequence(hand, n=5):
            return 5
        # Three of a Kind
        elif 3 in number_occurrences.values():
            return 4
        # Two Pairs
        elif list(number_occurrences.values()).count(2) == 2:
            return 3
        # One Pair
        elif 2 in number_occurrences.values():
            return 2
        # High Card
        else:
            return 1
