import behaviour
class Player:

	name = None
	hand = None
	behaviour = None
	fnCalculatePoint = None

	def __init__(self, n = "Unknown", fnCalculatePoint = lambda x: 0, behaviour = None):
		self.name = n
		self.hand = []
		self.fnCalculatePoint = fnCalculatePoint
		self.behaviour = behaviour and behaviour() or behaviour.HumanBehaviour()

	def __repr__(self):
		return "Player: %s\n" % self.name + str(self.hand)

	def getPoints(self):
		return self.fnCalculatePoint(self)
