from typing import List

from card import Card


class Hand:
    """Represents a hand of playing cards."""

    def __init__(self, cards: List[Card]) -> None:
        """
        Initialize a Hand object.

        Args:
            cards (List[Card]): The list of Card objects representing the hand.
        """
        self.cards = cards
        self._current_index = 0

    def __repr__(self) -> str:
        """
        Return a string representation of the hand.

        Returns:
            str: The string representation of the hand.
        """
        return f'{self.__class__.__name__}(cards={self.cards})'

    def __iter__(self):
        """
        Initialize the iterator for iterating over the cards in the hand.

        Returns:
            Hand: The Hand object itself as an iterator.
        """
        return self

    def __next__(self) -> Card:
        """
        Get the next card in the hand.

        Returns:
            Card: The next Card object in the hand.

        Raises:
            StopIteration: If there are no more cards to iterate over.
        """
        if self._current_index < len(self.cards):
            card = self.cards[self._current_index]
            self._current_index += 1
            return card

        self._current_index = 0
        raise StopIteration

    @classmethod
    def from_string(cls, str_hand: str) -> 'Hand':
        """
        Create a Hand object from a string representation of a hand.

        Args:
            str_hand (str): The string representation of a hand.

        Returns:
            Hand: The Hand object created from the string representation.

        Raises:
            Exception: If the input is not a string or the hand has an invalid number of cards.
        """
        if type(str_hand) != str:
            raise Exception(f"Invalid Input, the input should be a string")
            
        list_hand = str_hand.split()
        if len(list_hand) != 7:
            raise Exception(f"Invalid Hand of '{len(list_hand)}' cards, A valid hand must have 7 cards")

        cards = [Card.from_string(str_card) for str_card in list_hand]

        return Hand(cards)

    def get_highest_card(self) -> Card:
        """
        Get the highest card in the hand.

        Returns:
            Card: The highest Card object in the hand.
        """
        return max(self.cards)
