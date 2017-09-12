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
			print(game.getMessage(ERROR_MESSAGE_COMMAND_NOT_RECOGNIZED))

		return cmd

class DealerBehaviour(IBehaviour):

	def tick(self, player, game):

		if player.getPoints() < 17:
			return game.commands['hit']

		return game.commands['pass']

