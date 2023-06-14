from game import Game

game = Game.from_file('game_1.json')
winners = game.find_winner()

for winner in winners:
    print(winner)

