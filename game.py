import json

from typing import List, Dict

from hand import Hand
from player import Player
from ranking import HandRanking

class Game:

    def __init__(self, players: List[Player]) -> None:
        self.palyers = players

    def _get_players_with_highest_rank(self, player_rankings) -> Dict[Player, int]:

        players_with_highest_rank = { 
            key: value for key, value in player_rankings.items() \
            if value == max(player_rankings.values()) 
        }
        return players_with_highest_rank

    def _tie_breaker(self, players: Dict[Player, int]) -> List[Player]:
        
        pop = { player: player.hand.get_highest_card() for player in players.keys()}
        foo = { 
            key: value for key, value in pop.items() \
            if value == max(pop.values()) 
        }

        return list(foo.keys())

    @classmethod
    def from_file(cls, file_path: str) -> 'Game':

        with open(file_path) as f:
            game_data = json.load(f)
        players = [ Player.from_dict(player) for player in game_data['players'] ]
        
        return Game(players)

    def find_winner(self) -> List[Player]:

        player_rankings = { player: HandRanking.rank(player.hand) for player in self.palyers }
       
        # Tie Breaker
        players_with_highest_rank = self._get_players_with_highest_rank(player_rankings)
        if len(players_with_highest_rank) == 1:
            return list(players_with_highest_rank.keys())
        else:
            return self._tie_breaker(players_with_highest_rank)
        