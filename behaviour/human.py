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

	def tick(self, player, game):

		cmd = None
		while True:
			print('> ', end='')
			cmd = getCommand(input())
			if (cmd):
				break
			Message.print('ERROR_MESSAGE_COMMAND_NOT_RECOGNIZED')

		return cmd


