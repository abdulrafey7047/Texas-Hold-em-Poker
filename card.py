from utils import number_map, reverse_number_map, card_suits


class Card:
    """Represents a playing card."""

    def __init__(self, number: int, suit: str) -> None:
        """
        Initialize a Card object.

        Args:
            number (int): The number or rank of the card.
            suit (str): The suit of the card.
        """
        self.number = number
        self.suit = suit

    def __repr__(self) -> str:
        """
        Return a string representation of the card.

        Returns:
            str: The string representation of the card.
        """
        return f"{self.__class__.__name__}(number={reverse_number_map[self.number]}, suit={self.suit})"

    def __lt__(self, card: 'Card') -> bool:
        """
        Compare if the current card is less than the given card.

        Args:
            card (Card): The card to compare against.

        Returns:
            bool: True if the current card is less than the given card, False otherwise.
        """
        return self.number < card.number

    def __gt__(self, card: 'Card') -> bool:
        """
        Compare if the current card is greater than the given card.

        Args:
            card (Card): The card to compare against.

        Returns:
            bool: True if the current card is greater than the given card, False otherwise.
        """
        return self.number > card.number

    def __eq__(self, card: 'Card') -> bool:
        """
        Compare if the current card is equal to the given card.

        Args:
            card (Card): The card to compare against.

        Returns:
            bool: True if the current card is equal to the given card, False otherwise.
        """
        return self.number == card.number

    @classmethod
    def from_string(cls, str_card: str) -> 'Card':
        """
        Create a Card object from a string representation of a card.

        Args:
            str_card (str): The string representation of a card.

        Returns:
            Card: The Card object created from the string representation.

        Raises:
            Exception: If the input is not a string or the card number or suit is invalid.
        """
        if type(str_card) != str:
            raise Exception(f"Invalid Input, the input should be a string")

        number = number_map.get(str_card[0], None)
        suit = str_card[1]

        if number is None:
            raise Exception(f"Invalid Card Number: '{number}', Should be one of {list(number_map.keys())}")
        if not suit in card_suits:
            raise Exception(f"Invalid Card Suit: '{suit}', Should be one of {card_suits}")

        return Card(number, suit)