class Field():

  def __init__(self, data):
  """
    this class initializes a force field for this simulator
    e.g. the gravity field.

    @args uniform whether the force is uniform over the container
  """
  self.uniform = data[0]
  self.pos = data[1]
  self.force = data[2]
