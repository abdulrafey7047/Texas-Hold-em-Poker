from typing import Dict

from hand import Hand
from ranking import HandRanker


class Player:

    def __init__(self, id: str, hand: Hand) -> None:
        self.id = id
        self.hand = hand
        self.rank = self._rank_hand()

    def __repr__(self) -> str:
        return self.id

    def _rank_hand(self) -> int:
        return HandRanker.rank(self.hand)

    @classmethod
    def from_dict(cls, player_dict: Dict) -> 'Player':

        try:
            id = player_dict['id']
            hand = Hand.from_string(player_dict['hand'])
        except KeyError:
            raise Exception(f"Invalid player_dict format, expecting ['id', 'hand'] keys but got {list(player_dict.keys())}")
        
        return Player(id, hand)