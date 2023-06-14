from typing import List

from card import Card


class Hand:

    def __init__(self, cards: List[Card]) -> None:
        self.cards = cards
        self._current_index = 0

    def __repr__(self):
        return f'{self.__class__.__name__}(cards={self.cards})'
        

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
    def from_string(cls, str_hand: str) -> 'Hand':

        if type(str_hand) != str:
            raise Exception(f"Invalid Input, the input should be a string")
            
        list_hand = str_hand.split()
        if len(list_hand) != 7:
            raise Exception(f"Invalid Hand of '{len(list_hand)}' cards, A valid hand must have 7 cards")

        cards = [ Card.from_string(str_card) for str_card in list_hand ]

        print(Hand(cards))
        return Hand(cards)

    def get_highest_card(self):

        return max(self.cards)

