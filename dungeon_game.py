import random
import os
import sys
# draw grid
# pick random location for player
# pick random location for exit door
# pick random location for monster
# draw the player in the grid
# take input for movement
# move player, unless invalid move (past edges of the grid)
# check for win/lose
# clear the screen and redraw grid


CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0),
		 (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1),
		 (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2),
		 (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3),
		 (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
		 (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)]

def clear_screen():
	os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
	return random.sample(CELLS, 5)

def move_player(player, move):
	# Get the player position

	x, y = player

	if move == 'LEFT':
		x -= 1
	elif move == 'RIGHT':
		x += 1
	elif move == 'UP':
		y -= 1
	elif move == 'DOWN':
		y += 1

	# If move == 'LEFT', x - 1
	# If move == 'RIGHT', x + 1
	# If move == "UP", y-1
	# If move == "DOWN", y + 1

	return x, y

def move_monster(monster):
	
	
	x, y = random.choice(CELLS)

	return x, y	

def move_monster2(monster2):
	move_m = ['UP', 'DOWN', 'LEFT', 'RIGHT']
	x, y = monster2 
	if x == 0:
		move_m.remove('LEFT')
	if x == 5:
		move_m.remove('RIGHT')
	if y == 0:
		move_m.remove('UP')
	if y == 5:
		move_m.remove('DOWN')

	move_m_a = random.choice(move_m)
	
	if move_m_a == 'LEFT':
		x -= 1
	if move_m_a == 'RIGHT':
		x += 1
	if move_m_a == 'UP':
		y -= 1
	if move_m_a == 'DOWN':
		y += 1

	move_m = ['UP', 'DOWN', 'LEFT', 'RIGHT']
 
	if x == 0:
		move_m.remove('LEFT')
	if x == 5:
		move_m.remove('RIGHT')
	if y == 0:
		move_m.remove('UP')
	if y == 5:
		move_m.remove('DOWN')

	move_m_a = random.choice(move_m)
	
	if move_m_a == 'LEFT':
		x -= 1
	if move_m_a == 'RIGHT':
		x += 1
	if move_m_a == 'UP':
		y -= 1
	if move_m_a == 'DOWN':
		y += 1

	return x, y	

def move_monster3(monster3):
	move_m = ['UP', 'DOWN', 'LEFT', 'RIGHT']
	x, y = monster3 
	if x == 0:
		move_m.remove('LEFT')
	if x == 5:
		move_m.remove('RIGHT')
	if y == 0:
		move_m.remove('UP')
	if y == 5:
		move_m.remove('DOWN')

	move_m_a = random.choice(move_m)
	
	if move_m_a == 'LEFT':
		x -= 1
	if move_m_a == 'RIGHT':
		x += 1
	if move_m_a == 'UP':
		y -= 1
	if move_m_a == 'DOWN':
		y += 1

	move_m = ['UP', 'DOWN', 'LEFT', 'RIGHT']
 
	if x == 0:
		move_m.remove('LEFT')
	if x == 5:
		move_m.remove('RIGHT')
	if y == 0:
		move_m.remove('UP')
	if y == 5:
		move_m.remove('DOWN')

	move_m_a = random.choice(move_m)
	
	if move_m_a == 'LEFT':
		x -= 1
	if move_m_a == 'RIGHT':
		x += 1
	if move_m_a == 'UP':
		y -= 1
	if move_m_a == 'DOWN':
		y += 1		
			
	return x, y	

def get_moves(player):
	moves = ['LEFT', 'RIGHT', 'UP', 'DOWN']
	x, y = player

	if x == 0:
		moves.remove('LEFT')
	if x == 5:
		moves.remove('RIGHT')
	if y == 0:
		moves.remove('UP')
	if y == 5:
		moves.remove('DOWN')

	return moves


def draw_map(player, player_position, monster, monster2, monster3):
	clear_screen()
	print(" _"*6)
	tile = "|{}"

	for cell in CELLS:
		x, y = cell
		if x < 5:
			line_end = ""
			if cell == monster:
				output = tile.format("M")
			elif cell == monster2:
				output = tile.format("K")
			elif cell == monster3:
				output = tile.format("*")
			elif cell == player:
				output = tile.format("P")
			elif cell in player_position.values():
				output = tile.format(".")	
			else:
				output = tile.format("_")
		else:
			line_end = "\n"
			if cell == monster:
				output = tile.format("M|")
			elif cell == monster2:
				output = tile.format("K|")
			elif cell == monster3:
				output = tile.format("*|")
			elif cell == player:
				output = tile.format("P|")
			elif cell in player_position.values():
				output = tile.format(".|")
			else:
				output = tile.format("_|")
		print(output, end=line_end)	

def show_win():
	clear_screen()
	print(" _"*6)
	tile = "|{}"
	for cell in CELLS:
		x, y = cell
		
		if x < 5:
			x, y = cell
			end_line = ""
			output = tile.format("P")
		else:
			end_line = "\n"
			output = tile.format("P|")	
		print(output, end = end_line)

def show_lose():
	clear_screen()
	print(" _"*6)
	tile = "|{}"
	for cell in CELLS:
		
		x, y = cell
		if x < 5:
			end_line = ""
			output = tile.format("M")
		else:
			end_line = "\n"
			output = tile.format("M|")	
		print(output, end = end_line)


def game_loop():
	monster, monster2, monster3, door, player = get_locations()
	playing = True
	n = 0
	player_position = {n: player}

	

	while playing:
		draw_map(player, player_position, monster, monster2, monster3)
		valid_moves = get_moves(player)
		print("You are currently in room {}".format(player))	
		print("You can move {}".format(', '.join(valid_moves)))	
		print("Enter QUIT to quit")	

		move = input("> ")
		move = move.upper()

		if move == 'QUIT':
			print("\n ** See you next time! **\n")
			break

		if move in valid_moves:
			player = move_player(player, move)
			
			n += 1
			player_position.update({n: player})
			if player == monster or player == monster2 or player == monster3:
				show_lose()				
				print("\n ** Oh no! The monster got you. Better luck next time! **\n")
				playing = False
				
			elif player == door:
				show_win()				
				print("\n ** You escaped! Congratulation! **\n")
				playing = False
		else:
			input("\n ** Walls are hard, don't run into them! **\n")

		monster = move_monster(monster)
		monster2 = move_monster(monster2)
		monster3 = move_monster(monster3)
		if monster == player or monster2 == player or monster3 == player:	
				show_lose()			
				print("\n ** Oh no! The monster got you. Better luck next time! **\n")
				playing = False
	else:
		if input("Do you want to play again? [Y/n] ").lower() != 'n':
			game_loop()

		
	# Good move? Change the player position
	# Bad move? Don't change anything
	# On the door? They win
	# On the monster? They lose
	# Otherwise, loop back around 	


clear_screen()
print("Welcome to the Dungeon!\n")
print("""Direction: You're finding a way to escape the Dungeon.
	   There are 3 monsters in the Dungeon (M, K, *) and just only 1 hidden door.
	   You need to find the hidden door to escape!\n""")
input("Press return to start!")
clear_screen()
game_loop()


	