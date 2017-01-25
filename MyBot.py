import hlt
from hlt import NORTH, EAST, SOUTH, WEST, STILL, Move, Square
import random
import logging
logging.basicConfig(filename='MyBot.log',level=logging.DEBUG)
myID, game_map = hlt.get_init()
logging.info(game_map.width)
logging.info(game_map.height)
turn = 1

#find the highest production value on the map
topProd = 0
for square in game_map:
	if (square.production > topProd):
		topProd = square.production
logging.debug("Top Production: ")
logging.info(topProd)

		
#make a list of all the squares with the highest prouction values

hotSpots =  []	
for square in game_map:
	if (square.production == topProd):
		tup = (square.x, square.y)
		hotSpots.append(tup)
		
logging.debug("Got to end of hot spot list init.")
logging.debug(hotSpots)

#ISSUE IS WITH THIS LOOP
#for square in game_map
#	logging.info(square)
	#if square.owner == myID:
	#	logging.info(square)

#find the closest high value production square
HSdist = 999;
for x, y in hotSpots:
	logging.info(x)
	logging.info(y)
	#for square in game_map if square.owner == myID:
	#logging.info(square)
		#temp = hlt.get_distance(game_map, sq, x, y)
		#if(temp < HSdist):
			#HSdist = temp
			#closeHotSpot = sq
logging.info("Closest Hot Spot ")
#logging.info(closeHotSpot.x)
#logging.info(closeHotSpot.y)

hlt.send_init("HotSpotBot")


#if square has little strength, be still, if not random move to north or west
def assign_move(square):
	
	#dist = 99
	#tempDirection = direction
	for direction, neighbor in enumerate(game_map.neighbors(square)):
		if neighbor.owner != myID and (neighbor.strength + neighbor.production) < square.strength:
			#steer square towards closest hot spot early game
			#if (turn < 51):
			#	temp = hlt.get_distance(game_map, neighbor, square)
			#	if(dist > temp):
			#		dist = temp
			#		tempDirection = direction	
			#else:
				return Move(square, direction)

	if square.strength < 5 * square.production:
		return Move(square, STILL)
	else:
		return Move(square, random.choice((NORTH, WEST)))

while True:
	#update the current map
    game_map.get_frame()
	
	# If a piece is owned by us, let's instruct it to move according to assign_move
    moves = [assign_move(square) for square in game_map if square.owner == myID]
	
	# send all of our moves to the environment
    hlt.send_frame(moves)
	#turn++
