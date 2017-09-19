class Command:

	aliases = []

	def execute(self, player, game):
		raise NotImplementedError('Not implemented')
