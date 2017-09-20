from behaviour._base import Behaviour
import command

class ImplementedBehaviour(Behaviour):

  def bet(self, player, game):
    return 100

  def play(self, player, game):
    dealerScore = game.dealer.getPoints(True)
    playerScore = player.getPoints()

    if playerScore <= 11:
      return command.hit

    if playerScore == 12:
      if dealerScore == 4 or dealerScore == 5 or dealerScore == 5:
        return command.stand
      return command.hit

    if playerScore >= 13 and playerScore <= 16:
      if dealerScore <= 6:
        return command.stand
      return command.hit

    return command.stand
