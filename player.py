import behaviour as _behaviour
class Player:

	name = None
	hand = None
	behaviour = None
	game = None
	money = 0

	def __init__(self, game, name="Unknown", behaviourModule=_behaviour.human, money=1000):
		self.hand = []
		self.game = game
		self.name = name
		self.behaviour = behaviourModule.ImplementedBehaviour()
		self.money = money

	def __repr__(self):
		return "Player: %s ($%d)\n%s" % (self.name, self.money, self.hand)

	def getPoints(self, isInvisibleIgnored=False):
		return self.game.getPoints(self, isInvisibleIgnored)

	def hasFaceDownCard(self):
		cardInvisibilities = [not c.isVisible for c in self.hand]
		return any(cardInvisibilities)

	def bet(self, amount):
		self.money -= amount
		return self.money

	def gain(self, amount):
		self.money += amount
		return self.money
