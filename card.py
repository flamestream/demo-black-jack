class Card:

	number = None
	suit = None

	def __init__(self, n, s):
		self.number = n
		self.suit = s

	def __repr__(self):
		
		displayedNumber = None;
		if self.number == 1:
			displayedNumber = 'A'
		elif self.number == 11:
			displayedNumber = 'J'
		elif self.number == 12:
			displayedNumber = 'Q'
		elif self.number == 13:
			displayedNumber = 'K'
		else:
			displayedNumber = self.number

		displayedSuit = None
		if self.suit == 'hearts':
			displayedSuit = '♥'
		elif self.suit == 'clubs':
			displayedSuit = '♣'
		elif self.suit == 'diamonds':
			displayedSuit = '♦'
		elif self.suit == 'spades':
			displayedSuit = '♠'
		else:
			displayedSuit = '🂠'

		return '%s%s' % (displayedNumber, displayedSuit)