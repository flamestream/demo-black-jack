from behaviour.base import Behaviour
from message import Message

class HumanBehaviour(Behaviour):

	def tick(self, player, game):

		cmd = None
		while True:
			print('> ', end='')
			cmd = game.getCommand(input())
			if (cmd):
				break
			Message.print('ERROR_MESSAGE_COMMAND_NOT_RECOGNIZED')

		return cmd
