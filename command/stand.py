from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'pass',
		'end',
		'skip',
		'stop',
		'next',
		'stand'
	]

	def execute(self, player, game):
		print('%s has passed.' % player.name)
		return True

