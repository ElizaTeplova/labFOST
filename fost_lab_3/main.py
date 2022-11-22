import FallingObject
import FallingObjectBall
import FallingObjectHuman
import matplotlib.pyplot as plt


def main():

    choice = int(input("Enter your choice:\n1 - without parachute\n2 - with parachute\n3 - falling ball\n"))
    if choice == 1:
        human = FallingObjectHuman.FallingHuman()

        i = 0

        while human.getCurrentHigh(i) < 1200:
            i = i + 1
            human.getCurrentCoordinates(i)

        plt.figure(figsize=(13, 6))
        plt.subplot(121)
        plt.xlabel("time")
        plt.ylabel("high")
        plt.plot(human.getAllTimes(), human.getAllHighs())

        plt.subplot(122)
        plt.title("man without a parachute")
        plt.xlabel("time")
        plt.ylabel("speed")
        plt.plot(human.getAllTimes(), human.getAllSpeeds())
        plt.show()

    elif choice == 2:
        hWithP = FallingObjectHuman.FallingHuman()
        hWithP.setRadius()
        i = 0

        while i <= 60:
            i = i + 1
            hWithP.getCurrentCoordinates(i)

        plt.figure(figsize=(13, 6))
        plt.subplot(121)
        plt.xlabel("time")
        plt.ylabel("high")
        plt.plot(hWithP.getAllTimes(), hWithP.getAllHighs())

        plt.subplot(122)
        plt.title("man with a parachute")
        plt.xlabel("time")
        plt.ylabel("speed")
        plt.plot(hWithP.getAllTimes(), hWithP.getAllSpeeds())
        plt.show()

    else:
        ball = FallingObjectBall.FallingBall()
        i = 0

        while ball.getCurrentTime(i) <= 1:
            i = i + 1
            ball.getCurrentCoordinate(i)

        plt.figure(figsize=(13, 6))
        plt.subplot(121)
        plt.xlabel("time")
        plt.ylabel("high")
        plt.plot(ball.getAllTimes(), ball.getAllHighs())

        plt.subplot(122)
        plt.xlabel("time")
        plt.ylabel("speed")
        plt.plot(ball.getAllTimes(), ball.getAllSpeeds())
        plt.show()


if __name__ == '__main__':
    main()
