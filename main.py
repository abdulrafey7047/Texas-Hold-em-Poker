import sys
from game import Game


if len(sys.argv) != 2:
    print('Usage: python main.py <path_to/game_data_file.json>')
    sys.exit(1)

game_data_file_path = sys.argv[1]
try:
    game = Game.from_json(game_data_file_path)
except FileNotFoundError as e:
    print(e)
    sys.exit(1)

winners = game.find_winner()

for winner in winners:
    print(f'Winner: {winner}, Hand Rank: {winner.rank}')
