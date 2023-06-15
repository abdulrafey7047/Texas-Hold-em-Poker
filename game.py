import json

from typing import List

from player import Player

class Game:

    def __init__(self, players: List[Player]) -> None:
        self.players = players

    def _tie_breaker(self, players: List[Player]) -> List[Player]:
        
        highest_card = max([ player.hand.get_highest_card() for player in players] )
        winners = [
            player for player in self.players \
                if player.hand.get_highest_card() == highest_card
        ]
        return winners

    @classmethod
    def from_json(cls, file_path: str) -> 'Game':

        with open(file_path) as f:
            game_data = json.load(f)
        players = [ Player.from_dict(player) for player in game_data['players'] ]
        
        return Game(players)

    def find_winner(self) -> List[Player]:

        highest_player_rank = max(self.players, key=lambda player: player.rank).rank

        # Checking if multiple players have the highest rank
        players_with_highest_rank = [
            player for player in self.players \
                if player.rank == highest_player_rank
        ]
       
        # Tie Breaker
        if len(players_with_highest_rank) == 1:
            return list(players_with_highest_rank)
        else:
            return self._tie_breaker(players_with_highest_rank)
        