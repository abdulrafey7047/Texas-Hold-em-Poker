import json
from typing import List
from player import Player

class Game:
    """Represents a card game with multiple players."""

    def __init__(self, players: List[Player]) -> None:
        """
        Initialize a Game object.

        Args:
            players (List[Player]): A list of Player objects representing the players in the game.
        """
        self.players = players

    def _tie_breaker(self, players: List[Player]) -> List[Player]:
        """
        Perform a tie-breaker to determine the winner in case of a tie.

        Args:
            players (List[Player]): A list of Player objects with the same highest rank.

        Returns:
            List[Player]: A list of Player objects who are the winners after the tie-breaker.
        """
        highest_card = max([player.hand.get_highest_card() for player in players])
        winners = [
            player for player in self.players if player.hand.get_highest_card() == highest_card
        ]
        return winners

    @classmethod
    def from_json(cls, file_path: str) -> 'Game':
        """
        Create a Game object from a JSON file.

        Args:
            file_path (str): The path to the JSON file containing the game data.

        Returns:
            Game: A Game object created from the JSON data.

        Raises:
            FileNotFoundError: If the specified file_path does not exist.
            JSONDecodeError: If there is an error decoding the JSON data.
        """
        with open(file_path) as f:
            game_data = json.load(f)
        players = [Player.from_dict(player) for player in game_data['players']]
        
        return Game(players)

    def find_winner(self) -> List[Player]:
        """
        Find the winner(s) of the game based on the players' ranks.

        Returns:
            List[Player]: A list of Player objects who are the winners of the game.
        """
        highest_player_rank = max(self.players, key=lambda player: player.rank).rank

        # Checking if multiple players have the highest rank
        players_with_highest_rank = [
            player for player in self.players if player.rank == highest_player_rank
        ]
       
        # Tie Breaker
        if len(players_with_highest_rank) == 1:
            return list(players_with_highest_rank)
        else:
            return self._tie_breaker(players_with_highest_rank)
