from random import random

VALUES = {
	'ERROR_MESSAGE_COMMAND_NOT_RECOGNIZED': {
		'Command is not recognized. Please try again.': 9,
		'Wut?': 1,
		'Not sure that worked.': 1,
		'You must build additional pylons.': 1,
		"Try typing 'help'.": 3
	}
}

class Message:

	@staticmethod
	def get(id):

		choices = VALUES.get(id)
		if not choices:
			return ''

		indexes = []
		for k, v in choices.items():
			indexes += [k] * v

		targetIndex = int(random() * sum(choices.values()))
		msg = indexes[targetIndex]

		return msg

	@classmethod
	def print(cls, id):
		print(cls.get(id))
