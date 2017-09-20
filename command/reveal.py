from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'reveal',
		'show card',
		'face up'
	]

	def execute(self, player, game, params):
		hasRevealedCard = False
		for c in player.hand:
			if not c.isVisible:
				c.isVisible = True
				hasRevealedCard = True
		if hasRevealedCard:
			print('Revealing hand: %s' % player.hand)
		else:
			print("Nothing to reveal!")
