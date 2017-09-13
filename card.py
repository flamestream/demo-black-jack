SUITS = ('♥', '♣', '♦', '♠')
LABEL = {
	1: 'A',
	11: 'J',
	12: 'Q',
	13: 'K'
}

class Card:

	value = None
	suit = None
	isVisible = None

	def __init__(self, n, s, isVisible=False):
		self.value = n
		self.suit = s
		self.isVisible = isVisible

	def __repr__(self):

		if not self.isVisible:
			return '🂠'

		displayedValue = LABEL.get(self.value, self.value)
		return '%s%s' % (self.suit, displayedValue)

	@staticmethod
	def generateDeck(count=1, minValue=1, maxValue=13):

		if maxValue < minValue:
			raise ValueError('maxValue must not be lower than minValue')

		out = []
		++maxValue
		for i in range(0, count):
			for suit in SUITS:
				for n in range(minValue, maxValue):
					out.append(Card(n, suit))

		return out
