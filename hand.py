from typing import List

from card import Card

class Hand:

    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards
        self._current_index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._current_index < len(self.cards):
            card = self.cards[self._current_index]
            self._current_index += 1
            return card

        self._current_index = 0
        raise StopIteration

    @classmethod
    def from_string(cls, str_hand: List[str]) -> 'Hand':

        if len(str_hand) != 7:
            raise Exception("Invalid Hand")

        cards = list()
        for str_card in str_hand:
            cards.append(Card.from_string(str_card))

        return Hand(cards)

