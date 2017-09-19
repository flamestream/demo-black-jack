from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'hand',
		'view hand',
		'get hand'
	]

	def execute(self, player, game):
		print('Current hand: %s' % player.hand)

