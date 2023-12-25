import os

dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()


def partOne():
    return "monkey"


print(partOne())
