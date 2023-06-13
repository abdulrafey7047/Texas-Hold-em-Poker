import json

from typing import List, Dict

from hand import Hand
from player import Player
from ranking import HandRanking

class Game:

    def __init__(self, players: List[Player]) -> None:
        self.palyers = players

    def _get_players_with_highest_rank(self) -> Dict[Player, int]:
        pass

    def _tie_breaker(self) -> List[Player]:
        pass

    @classmethod
    def from_file(cls, file_path: str) -> 'Game':

        with open(file_path) as f:
            game_data = json.load(f)
    
        players = [ Player.from_dict(player) for player in game_data['players'] ]
        
        return Game(players)

    def find_winner(self) -> List[Player]:

        player_rankings = { player: HandRanking.rank(player.hand) for player in self.palyers }
       
        ## TODO: implement tie breaker logic
        players_with_highest_rank = self._get_players_with_highest_rank(player_rankings)

        if len(players_with_highest_rank) == 1:
            return list(players_with_highest_rank.keys())
        else:
            self._tie_breaker(players_with_highest_rank)
        