# Wumpus Game
# Aaron Lichtman
# December 2010

# Importing random function library.
import random

# Initialize the map array.
world =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
		[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# Hide the wumpus (w).
row = random.randint(1, 5)
col = random.randint(1, 8)
world[row][col] = 'w'

# Hide the pit (p).
needit = True
while needit:
	row = random.randint(1, 5)
	col = random.randint(1, 8)
	if world[row][col] == 0:
		world[row][col] = 'p'
		needit = False

# Hide the bat (b)
needit = True
while needit:
	row = random.randint(1, 5)
	col = random.randint(1, 8)
	if world[row][col] == 0:
		world[row][col] = 'b'
		needit = False

# Place the user in a safe spot.
needit = True
while needit:
	row = random.randint(1, 5)
	col = random.randint(1, 8)
	if world[row][col] == 0:
		userRow = row
		userCol = col
		needit = False

# Initialize variables
arrows = 5
alive = True

while alive:

	# Tell user where he is.
	print('You are at row ' + str(userRow) + ' and col ' + str(userCol) + '.')

	# Tells user if he is near the wumpus
	if world[userRow - 1][userCol] == 'w' or world[userRow + 1][userCol] == 'w' or world[userRow][userCol - 1] == 'w' or \
					world[userRow][userCol + 1] == 'w':
		print('I smell a Wumpus...  (Insert epic sound effects here)')

	# Tells user if he is near a pit
	if world[userRow - 1][userCol] == 'p' or world[userRow + 1][userCol] == 'p' or world[userRow][userCol - 1] == 'p' or \
					world[userRow][userCol + 1] == 'p':
		print('I feel a draft...  (Insert epic sound effects here)')

	# Tell the user if he is near a bat
	if world[userRow - 1][userCol] == 'b' or world[userRow + 1][userCol] == 'b' or world[userRow][userCol - 1] == 'b' or \
					world[userRow][userCol + 1] == 'b':
		print('I hear wings flapping...  (Insert epic sound effects here)')

	# Ask user what to do next (n/s/e/w/f).
	print('What do you want to do next?')
	print('You can type "n", "s", "e", or "w" to move, or "f" to fire an arrow.')
	action = input()

	# If direction, move
	if action == 'n':
		userRow = userRow - 1
	if action == 's':
		userRow = userRow + 1
	if action == 'e':
		userCol = userCol + 1
	if action == 'w':
		userCol = userCol - 1

	# Do not allow user to walk off the face of the Earth.
	if userRow == 0:
		userRow = 5
	elif userRow == 6:
		userRow = 1

	if userCol == 9:
		userCol = 1
	elif userCol == 0:
		userCol = 8

	# If wumpus then user dies.
	if world[userRow][userCol] == 'w':
		print('Chomp, chomp, chomp, you are dinner...')
		alive = 0

	# If pit then user dies.
	if world[userRow][userCol] == 'p':
		print('"Aaaaaaaaaah," you scream as you fall to your death.')
		alive = 0

	# If bat then hyperspace.
	if world[userRow][userCol] == 'b':

		print('You have been picked up by a bat.')

		needit = True
		while needit:
			row = random.randint(1, 5)
			col = random.randint(1, 8)
			if world[row][col] == 0:
				userRow = row
				userCol = col
				needit = False

	# Arrow/Shooting Stuff

	if action == 'f':
		print('Which direction do you want to fire?')
		flight = input()
		arrows = arrows - 1
		print('You have ' + str(arrows) + ' arrows left.')
		if arrows == 0:
			alive = False

		# Check if the arrow hit the wumpus.
		if flight == 'n':
			arrowRow = userRow - 1
			arrowCol = userCol
		if flight == 'e':
			arrowRow = userRow
			arrowCol = userCol + 1
		if flight == 's':
			arrowRow = userRow + 1
			arrowCol = userCol
		if flight == 'w':
			arrowRow = userRow
			arrowCol = userCol - 1

		# Do not allow the arrow to fly off the face of the Earth
		if arrowRow == 0:
			arrowRow = 5
		if arrowRow == 6:
			arrowRow = 1
		if arrowCol == 0:
			arrowCol = 8
		if arrowCol == 9:
			arrowCol = 1

		# Check what is in the spaces that he fired into.
		lookup = world[arrowRow][arrowCol]
		if lookup == 'w':
			print('You wumped the wumpus...')
			print('You win!!!!')
			alive = False
