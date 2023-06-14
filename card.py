from utils import number_map, reverse_number_map, card_suits


class Card:

    def __init__(self, number: int, suit: str) -> None:
        self.number = number
        self.suit = suit

    def __repr__(self):
        return f"{self.__class__.__name__}(number={reverse_number_map[self.number]}, suit={self.suit})"

    def __lt__(self, card: 'Card') -> bool:
        return self.number < card.number

    def __gt__(self, card: 'Card') -> bool:
        return self.number > card.number

    def __eq__(self, card: 'Card') -> bool:
        return self.number == card.number

    @classmethod
    def from_string(cls, str_card: str) -> 'Card':

        if type(str_card) != str:
            raise Exception(f"Invalid Input, the input should be a string")

        number = number_map.get(str_card[0], None)
        suit = str_card[1]

        if number is None:
            raise Exception(f"Invalid Card Number: '{number}', Should be one of {list(number_map.keys())}")
        if not suit in card_suits:
            raise Exception(f"Invalid Card Suit: '{suit}', Should be one of {card_suits}")

        return Card(number, suit)

