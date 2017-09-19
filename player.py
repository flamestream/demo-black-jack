import behaviour as _behaviour
class Player:

	name = None
	hand = None
	behaviour = None
	game = None

	def __init__(self, game, name = "Unknown", behaviourModule = _behaviour.human):
		self.hand = []
		self.game = game
		self.name = name
		self.behaviour = behaviourModule.ImplementedBehaviour() 

	def __repr__(self):
		return "Player: %s\n" % self.name + str(self.hand)

	def getPoints(self, isInvisibleIgnored=False):
		return self.game.getPoints(self, isInvisibleIgnored)
