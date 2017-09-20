from blackjack import BlackJack
import behaviour

game = BlackJack({
	'Ryan': behaviour.tryhard,
	'Duo': behaviour.human,
  'Meh': behaviour.basicStrat
})
game.start();
