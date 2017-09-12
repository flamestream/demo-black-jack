class ICommand:

	# Equivalent inputs to execute command
	aliases = []

	def execute(self, player, game):
		raise NotImplementedError('Not implemented')

class HitCommand(ICommand):

	aliases = [
		'hit',
		'hit me',
		'card',
		'give card',
		'request card',
		'draw'
	]

	def execute(self, player, game):
		player.hand.append(game.deck.pop())
		lastCard = player.hand[len(player.hand) - 1]
		print('Received %s (%s pts | %s cards)' % (lastCard, player.getPoints(), len(player.hand)))

class PassCommand(ICommand):

	aliases = [
		'pass',
		'end',
		'skip',
		'stop',
		'next'
	]

	def execute(self, player, game):
		print('%s has passed.' % player.name)
		return True

class GetScoreCommand(ICommand):

	aliases = [
		'score',
		'get score',
		'my score'
	]

	def execute(self, player, game):
		print('Current hand score: %s' % player.getPoints())

class ViewHandCommand(ICommand):

	aliases = [
		'hand',
		'view hand',
		'get hand'
	]

	def execute(self, player, game):
		print('Current hand: %s' % player.hand)

class HelpCommand(ICommand):

	aliases = [
		'help'
	]

	def execute(self, player, game):
		print('Available commands: %s' % ', '.join(game.getAvailableCommands()))
