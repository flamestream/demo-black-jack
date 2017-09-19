from pprint import pformat
from player import Player
from card import Card
import command
from random import randint
import behaviour


class BlackJack:

	dealer = None
	players = []
	deck = []

	def __init__(self, playerInfo):

		# Setup dealer
		self.dealer = Player(self, name='House', behaviourModule=behaviour.dealer)

		# Setup players
		for k, v in playerInfo.items():
			self.players.append(Player(self, name=k, behaviourModule=v))

		self.initDeck(5)

	def __repr__(self):
		out = ''
		for p in self.players:
			out += '%s (%s pts)\n' % (p.getPoints())

		out += str(self.deck)

		return out

	def initDeck(self, count=1):
		self.deck = Card.generateDeck(count)

	def shuffleDeck(self):
		for idx, val in enumerate(self.deck):
			target = randint(0, len(self.deck) - 1)
			self.deck[target], self.deck[idx] = self.deck[idx], self.deck[target]

	def emptyHands(self, isBackToDeck=True):
		for p in self.players + [self.dealer]:
			if isBackToDeck:
				self.deck += p.hand
			p.hand = []

	def reset(self):
		self.emptyHands()
		self.shuffleDeck()

	def dealCards(self, player, cardCount=1, isVisible=True):
		out = []
		for i in range(0, cardCount):
			card = self.deck.pop();
			card.isVisible = isVisible
			player.hand.append(card)
			out.append(card)
		return out

	def getResults(self):

		houseScore = self.dealer.getPoints()
		out = []
		for p in self.players:

			playerScore = p.getPoints()

			rate = 0
			if playerScore > 21:
				rate = 0
			elif len(p.hand) >= 5:
				rate = 2
			elif houseScore > 21:
				rate = 2
			elif playerScore == houseScore:
				rate = 1
			elif playerScore > houseScore:
				rate = 2

			out.append(rate)

		return out

	def declareResults(self):

		rates = self.getResults()
		results = {
			0: 'lost',
			1: 'pushed',
			2: 'won'
		}

		for idx, p in enumerate(self.players):
			print('%s %s.' % (p.name, results[rates[idx]]))

	def init(self):

		self.shuffleDeck()

		for i in range(0, 2):
			for p in self.players + [self.dealer]:
				# Special face-up action for last card of dealer
				isCardFaceDown = p == self.dealer and i == 1
				givenCards = self.dealCards(p, isVisible = not isCardFaceDown)
				print('Dealt %s to %s' % (givenCards, p.name))

		# for p in [self.dealer] + self.players:
		# 	print("%s's hand: %s" % (p.name, p.hand))

	def getPoints(self, player, isInvisibleIgnored=False):
		out = 0;
		visiblePlayerHand = [c for c in player.hand if not (not c.isVisible and isInvisibleIgnored)]
		cardsNotAce = [c for c in visiblePlayerHand if c.value != 1]
		valueWithoutAces = sum([min(c.value, 10) for c in cardsNotAce])
		aceCount = len(visiblePlayerHand) - len(cardsNotAce)

		out = valueWithoutAces;
		if aceCount:
			if 10 + aceCount + valueWithoutAces > 21:
				out += aceCount
			else:
				out += 10 + aceCount

		return out

	def start(self):

		self.init()

		for p in self.players + [self.dealer]:
			print("It's %s's turn." % p.name)
			while p.getPoints() <= 21:
				commandModule = p.behaviour.tick(p, self)
				command = commandModule.ImplementedCommand()
				if command.execute(p, self):
					break

		self.declareResults()
