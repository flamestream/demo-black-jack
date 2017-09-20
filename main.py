from blackjack import BlackJack
import behaviour

game = BlackJack({
	'Bot': behaviour.tryhard,
	'Rob': behaviour.basic,
	'Player': behaviour.human
})
game.start();
