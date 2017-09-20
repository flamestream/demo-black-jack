from blackjack import BlackJack
import behaviour

game = BlackJack({
	'Ryan': behaviour.dealer,
	'Duo': behaviour.human,
  'Et': behaviour.basicStrat
})
game.start();
