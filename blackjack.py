from pprint import pformat
from player import Player
from card import Card
import command
from random import random
from random import randint
import behaviour

class BlackJack:

	dealer = None
	players = []
	cards = {}
	deck = []
	commands = {}

	def __init__(self, playerInfo):

		def fnCalculatePoints(player):

			out = 0;

			cardsNotAce = [c for c in player.hand if c.number != 1]
			valueWithoutAces = sum([min(c.number, 10) for c in cardsNotAce])
			aceCount = len(player.hand) - len(cardsNotAce)

			out = valueWithoutAces;
			if aceCount >= 1:
				if 10 + aceCount + valueWithoutAces > 21:
					out += aceCount
				else:
					out += 10 + aceCount

			return out

		# Setup players
		self.dealer = Player('House', fnCalculatePoints, behaviour=behaviour.DealerBehaviour)

		for k, v in playerInfo.items():
			self.players.append(Player(k, fnCalculatePoints, behaviour=v))

		# Setup cards
		for n in range(1, 14):
			self.cards['s'+str(n)] = Card(n, 'spades')
		for n in range(1, 14):
			self.cards['h'+str(n)] = Card(n, 'hearts')
		for n in range(1, 14):
			self.cards['d'+str(n)] = Card(n, 'diamonds')
		for n in range(1, 14):
			self.cards['c'+str(n)] = Card(n, 'clubs')

		# Setup deck
		for i, c in self.cards.items():
			self.deck.append(c)

		# Register all available commands
		self.commands['help'] = command.HelpCommand()
		self.commands['hit'] = command.HitCommand()
		self.commands['pass'] = command.PassCommand()
		self.commands['score'] = command.GetScoreCommand()
		self.commands['hand'] = command.ViewHandCommand()

	def __repr__(self):
		out = ''
		for p in self.players:
			out += '%s (%s pts)\n' % (p.getPoints())

		out += str(self.deck)

		return out

	def shuffle(self):
		for idx, val in enumerate(self.deck):
			target = randint(0, len(self.deck) - 1)
			self.deck[target], self.deck[idx] = self.deck[idx], self.deck[target]

	def dealCards(self, numberOfCards):
		for i in range(0, numberOfCards):
			for player in self.players + [self.dealer]:
				print('Give ' + str(self.deck[len(self.deck) - 1]) + ' to ' + player.name)
				player.hand.append(self.deck.pop())

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

	def declareWinners(self):

		rates = self.getResults()
		results = {
			0: 'lost',
			1: 'pushed',
			2: 'won'
		}

		for idx, p in enumerate(self.players):
			print('%s has %s' % (p.name, results[rates[idx]]))

	def getCommand(self, i):

		i = i.lower()

		cmd = self.commands.get(i)
		if cmd:
			return cmd

		for k, cmd in self.commands.items():
			for alias in cmd.aliases:
				if i == alias:
					return cmd

	def getMessage(self, choices):

		indexes = []
		for k, v in choices.items():
			indexes += [k] * v

		targetIndex = int(random() * sum(choices.values()))
		msg = indexes[targetIndex]

		return msg

	def getAvailableCommands(self):

		return self.commands.keys()

	def start(self):

		self.shuffle()
		self.dealCards(2)

		for p in self.players + [self.dealer]:

			print("It's %s's turn." % p.name)

			while p.getPoints() <= 21:

				cmd = p.behaviour.tick(p, self)

				if cmd.execute(p, self):
					break


		self.declareWinners()
