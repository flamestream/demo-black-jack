from behaviour._base import Behaviour
import command

class ImplementedBehaviour(Behaviour):

	def tick(self, player, game):
		dealerScore = game.dealer.getPoints(True)
		playerScore = player.getPoints()

		if playerScore < 16 or playerScore < dealerScore:
			return command.hit

		return command.stand
