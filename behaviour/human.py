from behaviour._base import Behaviour
from message import Message
import command
import inspect

def getCommand(i):
	i = i.lower()

	cmd = getattr(command, i, None)
	if cmd:
		return cmd

	commandModules = [commandModule for fileName, commandModule in inspect.getmembers(command) if not fileName.startswith('_')]
	for module in commandModules:
		for alias in module.ImplementedCommand.aliases:
			if i == alias:
				return module

class ImplementedBehaviour(Behaviour):


	def bet(self, player, game):

		betAmount = 0
		print('Place your bet ($%s)' % player.money)

		while True:

			print('> $', end='')
			betAmount = input()

			# Check if valid number
			try:
				betAmount = int(betAmount)
				if betAmount <= 0:
					raise ValueError()
			except ValueError:
				Message.print('ERROR_MESSAGE_INVALID_BET_AMOUNT')
				continue

			# Check funds
			if betAmount > player.money:
				Message.print('ERROR_MESSAGE_INSUFFICIENT_FUNDS')
				continue

			break

		return betAmount

	def play(self, player, game):

		cmd = None
		while True:
			print('> ', end='')
			cmd = getCommand(input())
			if (cmd):
				break
			Message.print('ERROR_MESSAGE_COMMAND_NOT_RECOGNIZED')

		return cmd


