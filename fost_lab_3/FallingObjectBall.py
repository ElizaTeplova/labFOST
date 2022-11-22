import numpy as np
import FallingObject


g = 9.8


class FallingBall(FallingObject.Objects):

    def __init__(self):
        super(FallingBall, self).__init__()
        self.roBall = 7800
        self.roEnv = 1260
        self.r = 0.1
        self.k = 6 * np.pi * self.r * 1480
        self.m1 = 4 / 3 * np.power(self.r, 3) * np.pi * (self.roBall - self.roEnv)
        self.m = 4 / 3 * np.pi * np.power(self.r, 3) * self.roBall
        self.dt = 0.02

    def getCurrentCoordinate(self, i):
        self.cTime.append(self.cTime[i - 1] + self.dt)
        self.v.append(self.v[i - 1] + self.dt / 2 * ((self.m1 * g - self.k * self.v[i - 1]) / self.m +
                                                        (self.m1 * g - self.k * (self.v[i - 1] + self.dt * (
                                                                self.m1 * g - self.k * self.v[i - 1])
                                                                                 / self.m)) / self.m))
        self.y.append(self.y[i - 1] + self.v[i] * self.dt)
        self.showCurrentCoordinates(i)

