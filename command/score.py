from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'score',
		'get score',
		'my score'
	]

	def execute(self, player, game, params):
		print('Current hand score: %s' % player.getPoints())

