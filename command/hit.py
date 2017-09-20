from command._base import Command

class ImplementedCommand(Command):

	aliases = [
		'hit',
		'hit me',
		'card',
		'give card',
		'request card',
		'draw'
	]

	def execute(self, player, game, params):
		lastCards = game.dealCards(player)
		lastCardStrings = []
		for c in lastCards:
			lastCardStrings.append(str(c))
		lastCardsDealt = ", ".join(lastCardStrings)
		print('Received %s (%s pts | %s cards)' % (lastCardsDealt, player.getPoints(), len(player.hand)))

