from message import Message

class IBehaviour:

	def tick(self, player, game):
		raise NotImplementedError('Not implemented')

class HumanBehaviour(IBehaviour):

	def tick(self, player, game):

		cmd = None
		while True:
			print('> ', end='')
			cmd = game.getCommand(input())
			if (cmd):
				break
			Message.print('ERROR_MESSAGE_COMMAND_NOT_RECOGNIZED')

		return cmd

class DealerBehaviour(IBehaviour):

	def tick(self, player, game):

		if player.getPoints() < 17:
			return game.commands['hit']

		return game.commands['pass']

class TryHardBehaviour(IBehaviour):

	def tick(self, player, game):
		dealerScore = game.dealer.getPoints()
		playerScore = player.getPoints()

		if playerScore < 16 or playerScore < dealerScore:
			return game.commands['hit']

		return game.commands['pass']
