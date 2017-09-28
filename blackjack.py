from pprint import pformat
from player import Player
from card import Card
import command
from random import randint
import behaviour


class BlackJack:

	dealer = None
	players = None
	deck = None
	turnCount = None
	isPauseWanted = None

	def __init__(self, playerInfo, isPauseWanted=True):

		# Initial values
		self.players = []
		self.deck = []
		self.turnCount = 0

		self.isPauseWanted = isPauseWanted

		# Setup dealer
		self.dealer = Player(self, name='House', behaviourModule=behaviour.dealer, money=1000000)

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

	def reset(self, isBackToDeck=True):
		self.emptyHands(isBackToDeck)
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
		out = {}
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

			out[p] = rate

		return out

	def calculateGains(self, betAmounts):

		rates = self.getResults()
		gains = {}
		for p in self.players:

			betAmount = betAmounts[p]
			rate = rates[p]
			gainAmount = betAmount * rate

			if gainAmount:
				p.gain(gainAmount)
				self.dealer.gain(-gainAmount)
				gains[p] = gainAmount
			else:
				self.dealer.gain(betAmount)
				gains[p] = -betAmount

		return gains


	def declareResults(self, betAmounts):

		rates = self.getResults()
		gains = self.calculateGains(betAmounts)
		stats = {}
		results = {
			0: 'lost',
			1: 'pushed',
			2: 'won'
		}

		for player, gainAmount in gains.items():

			rate = rates[player]

			diffLabel = gainAmount and '$%d' % gainAmount or '-$%d' % betAmount
			stats[player] = {"outcome":rate, "diff":gainAmount}
			print('%s %s (%s)' % (player.name, results[rate], diffLabel))


		return stats

	def init(self):

		for i in range(0, 2):
			for p in self.players + [self.dealer]:
				# Special face-up action for last card of dealer
				isCardFaceDown = p == self.dealer and i == 1
				givenCards = self.dealCards(p, isVisible = not isCardFaceDown)
				print('Dealt %s to %s' % (givenCards, p.name))

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

	def placeBets(self):

		out = {}

		for p in self.players:
			betAmount = p.behaviour.bet(p, self)
			currentMoney = p.bet(betAmount)
			out[p] = betAmount
			print("%s has bet $%d (Funds: $%d)" % (p.name, betAmount, currentMoney))

		return out

	def tick(self):

		self.turnCount += 1
		print('== TURN %d ==' % self.turnCount)

		self.reset()
		self.init()

		betAmounts = self.placeBets()

		# Main playing loop
		for p in self.players + [self.dealer]:
			print("It's %s's turn" % p.name)
			while p.getPoints() <= 21:
				commandModule = p.behaviour.play(p, self)
				command = commandModule.ImplementedCommand()
				if command.execute(p, self, {}):
					break

		return self.declareResults(betAmounts)

	def start(self):

		while True:
			self.tick()
			self.isPauseWanted and input()

