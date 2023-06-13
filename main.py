from hand import Hand
from ranking import HandRanking

with open('input.in') as f:
    for input_str in f.readlines():

        input_hand = Hand.from_string(input_str.split())
        print(HandRanking.rank(input_hand))
