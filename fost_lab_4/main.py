import matplotlib.pyplot as plt
import Rocket


def main():
    rocket1 = Rocket.Rocket()
    i = 0

    while rocket1.tao[i] <= 1:
        i += 1
        rocket1.calcVH(i)

    rocket2 = Rocket.Rocket()
    rocket2.setA(0.3)
    i = 0

    while rocket2.tao[i] <= 1:
        i += 1
        rocket2.calcVH(i)

    rocket3 = Rocket.Rocket()
    rocket3.setA(0.4)
    i = 0

    while rocket3.tao[i] <= 1:
        i += 1
        rocket3.calcVH(i)

    rocket4 = Rocket.Rocket()
    rocket4.setA(0.5)
    i = 0

    while rocket4.tao[i] <= 1:
        i += 1
        rocket4.calcVH(i)

    plt.figure(figsize=(13, 6))
    plt.subplot(121)
    plt.xlabel("Tao")
    plt.ylabel("High")
    plt.title("H(t)")
    plt.grid()
    plt.plot(rocket1.getTaoList()[:1001], rocket1.getHList()[:1001])
    plt.plot(rocket2.getTaoList()[:1001], rocket2.getHList()[:1001])
    plt.plot(rocket3.getTaoList()[:1001], rocket3.getHList()[:1001])
    plt.plot(rocket4.getTaoList()[:1001], rocket4.getHList()[:1001])

    plt.subplot(122)
    plt.xlabel(r"$\tau$")
    plt.ylabel("Speed")
    plt.title("V(t)")
    plt.grid()
    plt.plot(rocket1.getTaoList()[:1001], rocket1.getVList()[:1001])
    plt.plot(rocket2.getTaoList()[:1001], rocket2.getVList()[:1001])
    plt.plot(rocket3.getTaoList()[:1001], rocket3.getVList()[:1001])
    plt.plot(rocket4.getTaoList()[:1001], rocket4.getVList()[:1001])

    plt.show()


    # print(len(rocket2.getTaoList()))
    # print(len(rocket2.getHList()))
    # print(len(rocket1.getTaoList()))
    # print(len(rocket1.getHList()))
    # plt.plot(rocket2.getTaoList()[:1001], rocket2.getHList()[:1001])
    # plt.plot(rocket2.getTaoList()[:1001], rocket2.getVList()[:1001])
    plt.show()


if __name__ == '__main__':
    main()
