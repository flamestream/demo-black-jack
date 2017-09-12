from blackjack import BlackJack
import behaviour

game = BlackJack({
	'Ryan': behaviour.DealerBehaviour,
	'Duo': behaviour.HumanBehaviour
})
game.start();
