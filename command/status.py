from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'status',
		'state'
	]

	def execute(self, player, game):
		print('Deck card count: %s' % len(game.deck))
		for p in [game.dealer] + game.players:
			print('%s\'s hand: %s with a hand score of %s points' % (p.name, p.hand, p.getPoints(True)))
