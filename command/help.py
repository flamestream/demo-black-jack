from command._base import Command
import command
import inspect

class ImplementedCommand(Command):

	aliases = [
		'help'
	]

	def execute(self, player, game, params):

		availableCommands = [name for name, obj in inspect.getmembers(command) if not name.startswith('_')]

		print('Available commands: %s' % ", ".join(availableCommands))




