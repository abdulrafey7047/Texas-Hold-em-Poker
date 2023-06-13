import json

from hand import Hand
from player import Player
from game import Game
from ranking import HandRanking

with open('game_1.json') as f:
    data = json.load(f)

# for player in data['players']:

#     # print((player['hand']))

#     player = Player.from_dict(player)
#     ranking = HandRanking.rank(player.hand)

#     print(ranking)


game = Game.from_file('game_1.json')

print(game.palyers)

print(game.find_winner())