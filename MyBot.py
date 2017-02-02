import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random

myID, game_map = hlt.get_init()
hlt.send_init("K2SOBot")


def find_nearest_enemy_direction(square):
    direction = NORTH
    max_distance = min(game_map.width, game_map.height) / 2
    for d in (NORTH, EAST, SOUTH, WEST):
        distance = 0
        current = square
        while current.owner == myID and distance < max_distance:
            distance += 1
            current = game_map.get_target(current, d)
        if distance < max_distance:
            direction = d
            max_distance = distance
    return direction

def heuristic(square):
	#default value of 1. Lower values means less likely to choose this action
	#currently prioritizing gaining territory over fighting. 
	#weak to an overly aggressive enemy
    if square.owner == 0 and square.strength > 0:
        return (square.production / square.strength)*100
    else:
        # return total potential damage caused by overkill when attacking this square
        return (sum(neighbor.strength for neighbor in game_map.neighbors(square) if neighbor.owner not in (0, myID)))*10

def get_move(square):
    target, direction = max(((neighbor, direction) for direction, neighbor in enumerate(game_map.neighbors(square))
                                if neighbor.owner != myID),
                                default = (None, None),
                                key = lambda t: heuristic(t[0]))
    if target is not None and target.strength < square.strength:
        return Move(square, direction)
	#base production multiplier is 5. Increased number means bots will be more
	#patient and grow more before moving out, thus stronger armies, but slower reinforcements and territory gain
    elif square.strength < square.production*4.9:
        return Move(square, STILL)

    border = any(neighbor.owner != myID for neighbor in game_map.neighbors(square))
    if not border:
        return Move(square, find_nearest_enemy_direction(square))
    else:
        #wait until we are strong enough to attack
        return Move(square, STILL)

    
while True:
    game_map.get_frame()
    moves = [get_move(square) for square in game_map if square.owner == myID]
    hlt.send_frame(moves)
	