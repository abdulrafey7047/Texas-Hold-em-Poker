from typing import Dict

from hand import Hand


class Player:

    def __init__(self, name: str, hand: Hand) -> None:
        self.name = name
        self.hand = hand

    def __repr__(self) -> str:
        return self.name

    @classmethod
    def from_dict(cls, player_dict: Dict) -> 'Player':

        try:
            name = player_dict['name']
            hand = Hand.from_string(player_dict['hand'])
        except KeyError:
            raise Exception(f"Invalid player_dict format, expecting ['name', 'hand'] keys but got {list(player_dict.keys())}")
        
        return Player(name, hand)