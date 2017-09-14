from behaviour.base import Behaviour

class TryHardBehaviour(Behaviour):

	def tick(self, player, game):
		dealerScore = game.dealer.getPoints()
		playerScore = player.getPoints()

		if playerScore < 16 or playerScore < dealerScore:
			return game.commands['hit']

		return game.commands['pass']
