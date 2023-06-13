from utils import number_map, reverse_number_map


class Card:

    def __init__(self, number: int, suit: str) -> None:
        self.number = number
        self.suit = suit

    def __repr__(self):
        return f'{reverse_number_map[self.number]}{self.suit}'

    @classmethod
    def from_string(cls, str_card: str) -> 'Card':
        number = number_map.get(str_card[0], None)
        suit = str_card[1]

        if number is None:
            raise Exception("Invalid Number")
        return Card(number, suit)

