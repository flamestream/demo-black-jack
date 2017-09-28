from blackjack import BlackJack
import behaviour

game = BlackJack({
	'Bot': behaviour.tryhard,
	'Rob': behaviour.basic,
	# 'Player': behaviour.human
})

roundMax = int(input("Welcome to the simulator, how many rounds shall it play? "))

playerStats = {}
roundCount = 1
for player in game.players:
	playerStats[player] = {"wins":0, "pushes":0, "losses":0, "moneyGain": 0}
results = []
while roundCount <= roundMax:
	results.append(game.tick())
	roundCount += 1
for rounds in results:
	for player, roundResults in rounds.items():
		if roundResults["outcome"] == 0:
			playerStats[player]["losses"] += 1
		elif roundResults["outcome"] == 1:
			playerStats[player]["pushes"] += 1
		elif roundResults["outcome"] == 2:
			playerStats[player]["wins"] += 1
		if roundResults["outcome"] != 1:
			if roundResults["outcome"] == 2:
				playerStats[player]["moneyGain"] += (roundResults["diff"]/2)
			else:
				playerStats[player]["moneyGain"] += (roundResults["diff"])

for player in playerStats:

