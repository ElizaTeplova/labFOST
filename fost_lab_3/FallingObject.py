class Objects:
    def __init__(self):
        self.cTime = [0.0]
        self.k = 0
        self.y = [0.0]
        self.v = [0.0]
        self.m = 0
        self.dt = 0.2
        self.ambientDensity = 0

    def getCurrentHigh(self, i):
        return self.y[i]

    def getCurrentSpeed(self, i):
        return self.v[i]

    def getAllHighs(self):
        return self.y

    def getAllSpeeds(self):
        return self.v

    def getAllTimes(self):
        return self.cTime

    def getCurrentTime(self, i):
        return self.cTime[i]

    def showCurrentCoordinates(self, i):
        print("i: %3d, y = %10.5f, v = %10.5f, cTime: %.2f" % (i - 1, self.y[i - 1], self.v[i - 1], self.cTime[i - 1]))
