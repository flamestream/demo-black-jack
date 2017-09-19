from behaviour._base import Behaviour
import command

class ImplementedBehaviour(Behaviour):

	def tick(self, player, game):
		if player.getPoints() < 17:
			return command.hit

		return command.stand
