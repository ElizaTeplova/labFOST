import matplotlib.pyplot as plt
import functions
import numpy as np
g = 9.81
#x = arr.array('d')

cObject = functions.Movement()

print("flight length: " + str(cObject.flightLength))
print("Max time: " + str(cObject.maxTime))

for i in range(1, functions.sizeOfArrays):
    cObject.currentCoordinatesWithoutWind(i)

wObject = functions.Movement()

# print("flight length: " + str(wObject.flightLength))
# print("Max time: " + str(wObject.maxTime))

# for i in range(1, functions.sizeOfArrays):
#     wObject.currentCoordinatesWithWind(i)
i = 0
while True:
    wObject.currentCoordinatesWithWind(i)
    i += 1
    if wObject.y[i] <= 0:
        break

plt.figure(figsize=(13, 6))
plt.subplot(131)
plt.plot(cObject.x, cObject.y)

plt.subplot(132)
plt.plot(wObject.x, wObject.y)
plt.suptitle("L - without wind, R - with wind")
plt.show()