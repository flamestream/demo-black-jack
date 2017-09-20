class Command:

	aliases = []

	def execute(self, player, game, params={}):
		raise NotImplementedError('Not implemented')
