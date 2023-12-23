import os
import math
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    timesString = lines[0].split(":")[1]
    distanceString = lines[1].split(":")[1]
    times = [int(number) for number in timesString.split()]
    distances = [int(number) for number in distanceString.split()]
    winCount = 0
    totalWinCount = 1
    for time in times:
        for i in range(time):
            print(f"time check: {(time-i)*i}")
            print(f"distance check: {distances[times.index(time)]}")
            if ((time-i)*i > distances[times.index(time)]):
                winCount += 1
            print(winCount)
        totalWinCount *= winCount
        winCount = 0
    return f"total win count: {totalWinCount}"

def partTwo():
    timesString = lines[0].split(":")[1]
    distanceString = lines[1].split(":")[1]
    time = int(timesString.replace(" ", ""))
    distance = int(distanceString.replace(" ", ""))
    print(f"testing debug: {((-time + math.sqrt(time**2-4*1*distance))/2) - ((-time - math.sqrt(time**2-4*1*distance))/2)}")
    print(f"total win count: {round(((-time + math.sqrt(time**2-4*1*distance))/2) - ((-time - math.sqrt(time**2-4*1*distance))/2))}")

# Plan for part one:
# Step 1: Get Time & Distance & put it into a 2D array
# Step 2: Iterate for length of time
# Step 3: If (time - i)*i > distance, increment potential wincases
# Step 4: At the end, multiply all potential wincases

# Plan for Part Two:
# i^2 + i*time + distance = 0

partTwo()
