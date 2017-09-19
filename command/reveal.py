from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'reveal',
		'show card',
		'face up'
	]

	def execute(self, player, game):
		for c in player.hand:
			if not c.isVisible:
				c.isVisible = True
		print('Revealing hand: %s' % player.hand)