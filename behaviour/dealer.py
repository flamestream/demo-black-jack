from behaviour.base import Behaviour

class DealerBehaviour(Behaviour):

	def tick(self, player, game):

		if player.getPoints() < 17:
			return game.commands['hit']

		return game.commands['pass']
