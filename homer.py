class Food:
    def __init__(self, name, expiration):
        self.name = name
        self.expiration = expiration


def openFridge(fridge):
    print("Following items are in Homer's fridge:")
    for food in fridge:
        print("{0} (expires in: {1} days)".format(
            str(food.name), str(food.expiration))
        )
    print("")

# Task 1
def maxExpirationDay(fridge):
    if len(fridge) == 0:
        return -1
    else:
        maxExDay = 0
        for food in fridge:
            if food.expiration > maxExDay:
                maxExDay = food.expiration
        return maxExDay

# Task 2
def histogramOfExpirations(fridge):
    histogram = []
    if len(fridge) == 0:
        return fridge
    maxDay = maxExpirationDay(fridge)
    for j in range(maxDay + 1):
        histogram.append(0)
    for i in range(maxDay + 1):
        for food in fridge:
            if i == food.expiration:
                histogram[i] += 1
    return histogram


# Task 3
def cumulativeSum(histogram):
    newHistogram = []
    sum = 0
    for i in range(len(histogram)):
        sum += histogram[i]
        newHistogram.append(sum)
    return newHistogram


# Task 4
def sortFoodInFridge(fridge):
    histogram = cumulativeSum(histogramOfExpirations(fridge))
    newFridge = []
    prevExpdate = 0
    for j in range(len(fridge)):
        newFridge.append(0)
    for i in range(len(fridge)):
        prevExpdate = fridge[i].expiration
        histogram[prevExpdate] -= 1
        poslnd = histogram[prevExpdate]
        newFridge[poslnd] = fridge[i]

    return newFridge


# Task 5
def reverseFridge(fridge):
    newFridge = []
    for i in range(len(fridge) - 1, -1, -1):
        newFridge.append(fridge[i])
    return newFridge

# Task 6
def eatFood(name, fridge):
    newFridge = []
    for i in fridge:
        newFridge.append(i)
    names = []
    prevFood = 0
    prevExpday = 800

    if len(newFridge) == 0:
        return newFridge

    for food in fridge:
        if food.name == name:
            names.append(food)
    if len(names) == 0:
        return newFridge
    else:
        for j in names:
            if j.name == name and j.expiration <= prevExpday:
                prevFood = j
                prevExpday = j.expiration
        newFridge.remove(prevFood)
        return newFridge


# print(openFridge(eatFood("donut0", [])))

# print(openFridge(eatFood("donut0",
#         [Food("donut9", 36), Food("donut9", 34), Food("donut0", 9),
#         Food("donut4", 35), Food("donut2", 26), Food("donut0", 45),
#         Food("donut6", 20), Food("donut8", 49), Food("donut2", 29),
#         Food("donut9", 8), Food("donut8", 41), Food("donut2", 39),
#         Food("donut8", 46)])))

# openFridge(eatFood("donut",
#         [Food("donut9", 36), Food("donut9", 34), Food("donut0", 9),
#         Food("donut4", 35), Food("donut2", 26), Food("donut0", 45),
#         Food("donut6", 20), Food("donut8", 49), Food("donut2", 29),
#         Food("donut9", 8), Food("donut8", 41), Food("donut2", 39),
#         Food("donut8", 46)]))

# openFridge(
#     eatFood("donut",
#         [Food("beer", 4), Food("steak", 1), Food("hamburger", 1),
#         Food("donut", 3), Food("donut", 1), Food("donut", 6)]
#     ))