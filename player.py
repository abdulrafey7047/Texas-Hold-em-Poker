from typing import Dict
from hand import Hand
from ranking import HandRanker


class Player:
    """Represents a player in a card game."""

    def __init__(self, id: str, hand: Hand) -> None:
        """
        Initialize a Player object.

        Args:
            id (str): The id of the player.
            hand (Hand): The Hand object representing the player's hand of cards.
        """
        self.id = id
        self.hand = hand
        self.rank = self._rank_hand()

    def __repr__(self) -> str:
        """
        Return a string representation of the player.

        Returns:
            str: The name of the player.
        """
        return self.id

    def _rank_hand(self) -> int:
        """
        Rank the player's hand using the HandRanker class.

        Returns:
            int: The rank of the player's hand.
        """
        return HandRanker.rank(self.hand)

    @classmethod
    def from_dict(cls, player_dict: Dict) -> 'Player':
        """
        Create a Player object from a dictionary.

        Args:
            player_dict (Dict): A dictionary containing the player's information.

        Returns:
            Player: A Player object created from the dictionary.

        Raises:
            Exception: If the player_dict does not have the expected format.
        """
        try:
            id = player_dict['id']
            hand = Hand.from_string(player_dict['hand'])
        except KeyError:
            raise Exception(f"Invalid player_dict format, expecting ['id', 'hand'] keys but got {list(player_dict.keys())}")

        return Player(id, hand)
