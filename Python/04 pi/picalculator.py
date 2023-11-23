import math


def newtonPi(init):
    cha = init
    x = 0
    diff = 1

    while diff != 0:
        x = cha - (math.sin(cha) / math.cos(cha))
        diff = cha - x
        cha = x
    return x


def leibnizPi(iterations):
    pi = 0
    n = 1

    for i in range(iterations):
        pi += ((-1) ** i) * (4 / n)
        n += 2
    return pi


def nilakanthaPi(iterations):
    pi = 3
    n = 2

    for i in range(iterations - 1):
        pi += ((-1) ** i) * (4 / (n * (n + 1) * (n + 2)))
        n += 2
    return pi

