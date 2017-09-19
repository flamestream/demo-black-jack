import behaviour
class Player:

	name = None
	hand = None
	behaviour = None
	game = None

	def __init__(self, game, name = "Unknown", behaviour = None):
		self.hand = []
		self.game = game
		self.name = name
		self.behaviour = behaviour or behaviour.human

	def __repr__(self):
		return "Player: %s\n" % self.name + str(self.hand)

	def getPoints(self, isInvisibleIgnored=False):
		return self.game.getPoints(self, isInvisibleIgnored)
