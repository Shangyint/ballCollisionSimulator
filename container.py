import numpy as np

class Container(object):
    """
    Container is either a 2d plate or a 3d box
    """

    def __init__(self, args):
        """
        dim should be either 2 or 3
        x, y, and z are the boundaries of the container
        """
        super(Container, self).__init__()
        self.dimension = args[0]
        self.x = args[1]
        self.y = args[2]
        self.lower_bound = [0, 0,]
        self.upper_bound = [self.x, self.y,]
        if self.dimension == 3:
            self.z = args[3]
            self.lower_bound.append(0)
            self.upper_bound.append(self.z)
