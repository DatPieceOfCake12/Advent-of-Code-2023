import os

dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()


def partOne():
    totalSum = 0
    for line in lines:
        numbersList = list()
        initList = [int(num) for num in line.split()]
        isChanging = True
        numbersList.append(initList)
        while isChanging:
            newList = list()
            for number in range(len(numbersList[-1]) - 1):
                difference = numbersList[-1][number + 1] - numbersList[-1][number]
                newList.append(difference)
            numbersList.append(newList)
            if newList == [0] * len(newList):
                isChanging = False
            print(newList)
        for i in range(len(numbersList) - 1, 0, -1):
            print(f"1: {numbersList[i-1]}")
            print(f"2: {numbersList[i]}")
            print(f"3: {numbersList[i - 1][-1] + numbersList[i][-1]}")
            numbersList[i - 1].append(numbersList[i - 1][-1] + numbersList[i][-1])
        totalSum += numbersList[0][-1]
    return f"totalsum: {totalSum}"


def partTwo():
    totalSum = 0
    for line in lines:
        numbersList = list()
        initList = [int(num) for num in line.split()]
        isChanging = True
        numbersList.append(initList)
        while isChanging:
            newList = list()
            for number in range(len(numbersList[-1]) - 1):
                difference = numbersList[-1][number + 1] - numbersList[-1][number]
                newList.append(difference)
            numbersList.append(newList)
            if newList == [0] * len(newList):
                isChanging = False
            print(newList)
        for i in range(len(numbersList) - 1, 0, -1):
            print(f"1: {numbersList[i-1]}")
            print(f"2: {numbersList[i]}")
            print(f"3: {numbersList[i - 1][0] - numbersList[i][0]}")
            numbersList[i - 1].insert(0, numbersList[i - 1][0] - numbersList[i][0])
        totalSum += numbersList[0][0]
    return f"totalsum: {totalSum}"


# Final Outcome: 2 Stars

print(partTwo())
