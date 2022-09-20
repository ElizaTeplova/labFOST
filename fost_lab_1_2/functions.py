import numpy as np
sizeOfArrays = 100
g = 9.81


class Movement:
    def __init__(self):
        self.speed = float(input("Enter starting speed of object: "))
        self.alpha = float(input("Enter starting angle of object: "))
        # self.x = np.zeros(sizeOfArrays)
        # self.y = np.zeros(sizeOfArrays)
        self.x = [0]
        self.y = [0]
        self.maxTime = (2 * self.speed * np.sin(self.alpha * np.pi / 180)) / g
        self.currentTime = 0
        self.flightLength = (self.speed * self.speed * np.sin(2 * self.alpha * np.pi / 180)) / g
        self.k = 2
        self.m = 1

    def currentCoordinatesWithoutWind(self, i):
        self.currentTime += self.maxTime / (sizeOfArrays - 1)
        # self.x[i] = self.speed * np.cos(self.alpha * np.pi / 180) * self.currentTime
        # self.y[i] = self.speed * np.sin(self.alpha * np.pi / 180) * self.currentTime - (
        #            g * self.currentTime * self.currentTime) / 2
        self.x.append(self.speed * np.cos(self.alpha * np.pi / 180) * self.currentTime)
        self.y.append(self.speed * np.sin(self.alpha * np.pi / 180) * self.currentTime - (
                g * self.currentTime * self.currentTime) / 2)
        print("%3d| ctime: %7.5f | x: %7.4f | y: %7.4f" % (i, self.currentTime, self.x[i], self.y[i]))
        #print(str(i) + "| ctime: " + str(self.currentTime) + " | x: " + str(self.x[i]) + " | y: " + str(self.y[i]))

    def currentCoordinatesWithWind(self, i):
        self.currentTime += 0.1
        self.x.append((self.speed * np.cos(self.alpha * np.pi / 180) * self.m * (
                1 - np.exp(-self.k * self.currentTime / self.m))) / self.k)
        self.y.append(self.m * ((self.speed * np.sin(self.alpha * np.pi / 180)) * (
                1 - np.exp(-self.k * self.currentTime / self.m)) - g * self.currentTime) / self.k)

        # self.x[i] = (self.windSpeed * np.cos(self.windAlpha * np.pi / 180) * self.m * (
        #             1 - np.exp(-self.k * self.currentTime / self.m))) / self.k
        #
        # self.y[i] = self.m * ((self.speed * np.sin(self.alpha * np.pi / 180)) * (
        #             1 - np.exp(-self.k * self.currentTime / self.m)) - g * self.currentTime) / self.k
        print("%3d| ctime: %7.5f | x: %7.4f | y: %7.4f" % (i, self.currentTime, self.x[i], self.y[i]))


    # def appendToArray(self):
    #     self.currentTime += self.maxTime / sizeOfArrays
