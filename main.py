import json

from game import Game
from player import Player

game = Game.from_json('game_1.json')
winners = game.find_winner()

for winner in winners:
    print(winner)


# with open('game_1.json') as f:
#     game_data = json.load(f)


# for player_data in game_data['players']:

#     player = Player.from_dict(player_data)
#     print(player.hand.get_highest_card().number)
