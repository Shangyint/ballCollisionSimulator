import numpy as np

class Ball(object):
    """
    @properties
        pos is position
        v is velocity
        r is radius
        m is mass
    """
    def __init__(self, args):
        super(Ball, self).__init__()
        self.pos = np.asarray(args[0], np.double)
        self.v = np.asarray(args[1], np.double)
        self.r = args[2]
        self.m = args[3]
        self.acc = np.asarray(args[4], np.double)

    def update(self, t=1):
        """
        @brief update the ball's postion based on time elapsed
        
        @param t = timer_fired
        """
        self.pos = np.add(self.pos, t * self.v + self.acc * (1/2 * t ** 2))
        self.v = np.add(self.v, t * self.acc)

