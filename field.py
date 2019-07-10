import numpy as np

class Field(object):
	"""docstring for Field"""
	def __init__(self, arg):
		super(Field, self).__init__()
		self.name = arg[0]
		self.dim = arg[1]
		self.type = arg[2]
		if self.name == "force":
			self.force = np.asarray(arg[3], np.double)
		elif self.name == "acceleration":
			self.acc = np.asarray(arg[3], np.double)
