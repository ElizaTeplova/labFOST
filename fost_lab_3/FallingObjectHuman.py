import numpy as np

import FallingObject

g = 10


class FallingHuman(FallingObject.Objects):
    def __init__(self):
        super(FallingHuman, self).__init__()
        self.ambientDensity = 1.22
        self.m = 65
        self.__high = 1.65
        self.__bodyGirth = 0.35
        self.k = self.ambientDensity * self.__high * self.__bodyGirth * 0.5
        self.dt = 0.2

    def getCurrentCoordinates(self, i):
        self.v.append(self.v[i - 1] + self.dt / 2 * ((self.m * g - self.k * self.v[i - 1] * self.v[i - 1]) / self.m + (
                    self.m * g - self.k * (self.v[i - 1] + self.dt * (
                        self.m * g - self.k * self.v[i - 1] * self.v[i - 1]) / self.m) ** 2) / self.m))
        self.y.append(self.y[i - 1] + self.v[i] * self.dt)
        self.cTime.append(self.cTime[i - 1] + self.dt)
        self.showCurrentCoordinates(i)

    def setRadius(self):
        r = 2.5
        self.k = np.pi * r * r
