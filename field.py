import numpy as np

class Field(object):
	"""docstring for Field"""
	def __init__(self, arg):
		super(Field, self).__init__()
		self.name = arg[0]
		self.dim = arg[1]
		if self.name == "gravity":
			self.type = "uniform"
			if self.dim == 2:
				self.acc = np.asarray([0, 10])
			else:
				self.acc = np.asarray([0, 0, 10])
			return
		self.type = arg[2]
		self.force = np.asarray(arg[3], np.double)
		