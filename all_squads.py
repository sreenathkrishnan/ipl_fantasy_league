

from squad import *
import random

data_file = "data/players.csv"

players = []
with open(data_file) as f:
    f.readline()
    for line in f.readlines():
        parts = line.strip().split(',')
        player = Player(id=int(parts[0]), 
            name=parts[1], 
            team=parts[2], 
            price=int(parts[3]), 
            role=parts[4],
            overseas=int(parts[5]) == 1,
            keeper=int(parts[6])==1,
            uncapped=int(parts[7])==1)
        players.append(player)

nplayers = len(players)
squad = random.sample(range(nplayers), 11)
print_squad_stats(squad, players) 