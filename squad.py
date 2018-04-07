
from collections import namedtuple

# A squad is valid if it hads
# 1. 11 Players
# 2. 5-6 Bat (including WK)
# 3. > 1 WK
# 4. 1-4 AR
# 5. 2-5 Bowl
# 6. Max 6 per franchise
# 7. Max 4 overseas
# 8. >= 1 uncapped
# 9. < 10 Million

Player = namedtuple('Player', ['id', 'name', 'team', 'price', 'role', 'overseas', 'keeper', 'uncapped'])

def is_squad_valid(squad, players):
    return (count_players(squad) == 11) and \
        (count_batsmen(squad, players) in [5, 6]) and \
        (count_keepers(squad, players) >= 1) and  \
        (count_all_rounders(squad, players) in [1, 2, 3, 4]) and \
        (count_bowlers(squad, players) in [2, 3, 4, 5]) and \
        (count_max_team(squad, players) <= 6) and \
        (count_overseas(squad, players) <= 4) and \
        (count_uncapped(squad, players) >= 1) and \
        (count_squad_price(squad, players) <= 10000000)

def print_squad_stats(squad, players):
    print "Players =", [players[pid].name for pid in squad]
    print "#Players = ", count_players(squad)
    print "Batsmen = ", count_batsmen(squad, players)
    print "Keepers = ", count_keepers(squad, players)
    print "All-rounders = ", count_all_rounders(squad, players)
    print "Max franchise =", count_max_team(squad, players)
    print "Overseas = ", count_overseas(squad, players)
    print "Uncapped = ", count_uncapped(squad, players)
    print "Price = ", count_squad_price(squad, players)
    print "Valid = ", is_squad_valid(squad, players)


def count_players(squad):
    return len(set(squad))

def count_batsmen(squad, players):
    return count_role(squad, players, "Bat")

def count_bowlers(squad, players):
    return count_role(squad, players, "Bowl")

def count_all_rounders(squad, players):
    return count_role(squad, players, "AR")

def count_keepers(squad, players):
    return sum([1 for pid in squad if players[pid].keeper])

def count_max_team(squad, players):
    d = {}
    for pid in squad:
        d[players[pid].team] = d.get(players[pid].team, 0) + 1
    return max(d.values())

def count_overseas(squad, players):
    return sum([1 for pid in squad if players[pid].overseas])

def count_uncapped(squad, players):
    return sum([1 for pid in squad if players[pid].uncapped])

def count_squad_price(squad, players):
    return sum([players[pid].price for pid in squad])


def count_role(squad, players, role):
    return sum([1 for pid in squad if players[pid].role==role])