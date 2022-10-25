import numpy as np

g = 9.8
beta = 2.3026
p0 = 1.27
t = 150
hMax = 17000
vMax = 7800
c = 0.4


class Rocket:

    tao = [0.0]

    def __init__(self):
        self.m0 = 300_000
        self.mEnd = 20_000
        self.S = 2 * np.pi * 5.5 * 50 + np.pi * 5.5 ** 2
        self.h = [0.0]
        self.v = [0.0]
        # self.tao = [0.0]
        self.k = self.mEnd / self.m0
        # self.k = 0.06666666666666667
        self.b = (t * g) / vMax
        self.p = 0.5 * p0 * c * self.S * vMax * t / self.m0 / 10
        self.a = 0.2
        self.e = vMax * t / hMax
        self.dt = 0.001

    def f(self, i):
        if self.tao[i] <= 1:
            return 1 - (1 - self.k) * self.tao[i]
        else:
            return self.k

    # def calcFormula(self, i, vi):
    #     fi = self.f(i)
    #     return (self.a - self.b * fi - self.p * np.exp(-beta * self.h[i]) * vi * vi) / fi
    #
    # def calcVH(self, i):
    #     self.tao.append(self.tao[i - 1] + self.dt)
    #     #V + dt * 0.5 * abs(dVdTau(tau, a, b, p, H, V, k) + dVdTau(tau, a, b, p, H, V + dt * dVdTau(tau, a, b, p, H, V, k), k))
    #     self.v.append(self.v[i - 1] + self.dt / 2 * abs(self.calcFormula(i - 1, self.v[i - 1] + self.calcFormula(i - 1, self.v[i - 1] + self.dt * self.calcFormula(i - 1, self.v[i - 1])))))
    #     self.h.append(self.h[i - 1] + self.e * self.v[i - 1] * self.dt)
    #     print("i: %d\ttao: %f\tv = %f\th = %f" % (i, self.tao[i], self.v[i], self.h[i]))

    def calcFormula(self, i, vi):
        return (self.a - self.b * self.f(i) - self.p * np.exp(-beta * self.h[i]) * vi * vi) / self.f(i)

    def calcVH(self, i):
        self.tao.append(self.tao[i - 1] + self.dt)
        self.v.append(self.v[i - 1] + (self.dt / 2) * abs(self.calcFormula(i - 1, self.v[i - 1]) +
                                                          self.calcFormula(i - 1, self.v[i - 1] + self.dt * self.calcFormula(i - 1, self.v[i - 1]))))
        self.h.append(self.h[i - 1] + self.e * self.v[i - 1] * self.dt)
        # print("i: %d\ttao: %f\tv = %f\th = %f" % (i, self.tao[i], self.v[i], self.h[i]))

    def setA(self, a):
        self.a = a

    def getTao(self, i):
        return self.tao[i]

    def getHList(self):
        return self.h

    def getVList(self):
        return self.v

    def getTaoList(self):
        return self.tao
