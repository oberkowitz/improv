from random import shuffle

#something.html and something_else.html are in Oren/mytest/templates

class Game:
	totalSlots = 0
	totalGames = 0
	fullGames = 0
	games = {}
	def __init__(self,name, size):
		self.players = []
		self.size = size
		self.full = False
		self.name = name
		Game.totalSlots += size
		Game.totalGames+=1
		Game.games[name] = self
	def printPlayers():
		for pname in players:
			print(pname)
	def isFull(self):
		if self.size+1 == len(self.players):
			self.full = True
			Game.fullGames+=1
		if self.size == len(self.players):
			self.full = True
		#print(self.name + " is full? " + str(self.full))
		return self.full
class Player:
	assigned = 0
	players = []
	def __init__(self,name,preferences): #preferences for all players total must be greater than number of total slots
		self.preferences = preferences
		self.games = []
		self.name = name
		Player.players.append(self)
	def addGame(self): #adds the top possible priority to a players list of games
		while len(self.preferences) > 0:
			game = Game.games[self.preferences.pop(0)]
			if not game.isFull():
				self.games.append(game.name)
				game.players.append(self.name)
				break

def main():
	#Game Names
	SI = "Sing It"
	NR = 'Naive Replay'
	GR = 'Genre Rollercoaster'
	NC = "New Choice"

	#Game declarations

	Game('Genre Rollercoaster', 4)
	Game('New Choice', 2)
	Game('Sing It', 3)
	Game('Naive Replay', 4)


	"""
	More games could go here
	"""
	#Player declarations
	Player("Chloe", [SI,NR]),
	Player("Mike", [NR,NC,SI]),
	Player("David", [GR,NC,SI,NR]),
	Player("Adam", [SI,GR,NC,NR]),
	Player("Madeeha", [NR,GR,SI]),
	Player("Michael", [GR,SI]),
	#Player("Emily", [GR,NC,SI]),
	Player("Camille", [GR, NR, NC]),
	Player("Megan", [GR,SI]),
	Player("Vanessa", [GR,NR]),
	Player("Jake", [NC, NR, GR, SI]),
	Player("Fernando", [GR,NC,SI]),
	Player("Oren", [NR,GR,NC])

	showSlots = 10

	# Game.games.shuffle()
	# count = 0
	# for game in Game.games:
	# 	if game.size + count < 

	totalSlots = Game.totalSlots

	players = Player.players

	shuffle(players)


	i = 0
	while i < totalSlots:
		for player in players:
			if Game.totalGames == Game.fullGames:
				break
			player.addGame()
		players.reverse()
		i+=1

	with open("games1.txt", "w") as out:
		out.write("Printing games:")
		for game in Game.games.values(): # out.write the games and their players
			out.write(game.name + " has these players: " + str(game.players)+"\n")

		out.write("\nPrinting players:")
		for player in players:
			out.write(player.name + " is in these games: " + str(player.games)+"\n")



