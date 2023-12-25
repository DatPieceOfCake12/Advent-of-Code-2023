import os

dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()


def keepLower(num1, num2):
    if num1 == 0:
        return num2
    if num2 == 0:
        return num1
    if num1 < num2:
        return num1
    else:
        return num2


def partOne():
    instructions = lines[0].replace("\n", "")
    keyRow, leftRow, rightRow = (
        list(),
        list(),
        list(),
    )
    for line in lines[3:]:
        keyRow.append(line[:3])
        leftRow.append(line[7:10])
        rightRow.append(line[12:15])
    instructIterator = 0
    keyIterator = keyRow.index("AAA")
    reachedGoal = False
    while not reachedGoal:
        currentLine = keyRow[keyIterator]
        print(f"currentLine: {currentLine}")
        print(f"iterator: {instructIterator}")
        print(f"instructor: {instructIterator % (len(instructions))},{instructions[instructIterator % len(instructions)]}")
        match instructions[instructIterator % len(instructions)]:
            case "R":
                currentLine = rightRow[keyIterator]
            case "L":
                currentLine = leftRow[keyIterator]
            case _:
                print("error: no value")
        if currentLine == "ZZZ":
            reachedGoal = True
        else:
            instructIterator += 1
            keyIterator = keyRow.index(currentLine)
        # get keyIterator index num
        # check instructions line
        # go to corresponding array w/ same index
        # find string
        # check string for zzz
        # repeat
    return instructIterator + 1


def partTwo():
    instructions = lines[0].replace("\n", "")
    (
        keyRow,
        leftRow,
        rightRow,
        keyIterators,
        keyRepeats,
    ) = (
        list(),
        list(),
        list(),
        list(),
        list(),
    )
    for line in lines[2:]:
        keyRow.append(line[:3])
        leftRow.append(line[7:10])
        rightRow.append(line[12:15])
    instructIterator = 0
    for item in range(len(keyRow)):
        if keyRow[item][-1] == "A":
            keyIterators.append(item)
    keyRepeats = [0] * len(keyIterators)
    reachedGoal = False
    fullRepeats = False
    bababooey = 0
    while not reachedGoal:
        for keyIterator in keyIterators:
            currentLine = keyRow[keyIterator]
            print(f"currentLine: {currentLine}")
            print(f"iterator: {instructIterator}")
            print(f"instructor: {instructIterator % (len(instructions))},{instructions[instructIterator % len(instructions)]}")
            match instructions[instructIterator % len(instructions)]:
                case "R":
                    currentLine = rightRow[keyIterator]
                case "L":
                    currentLine = leftRow[keyIterator]
                case _:
                    print("error: no value")
            keyIterators[keyIterators.index(keyIterator)] = keyRow.index(currentLine)
            if currentLine[-1] == "Z":
                keyRepeats[keyIterators.index(keyRow.index(currentLine))] = keepLower(
                    instructIterator,
                    keyRepeats[keyIterators.index(keyRow.index(currentLine))],
                )
        reachedGoal = True
        for keyIterator in keyIterators:
            if keyRow[keyIterator][-1] != "Z":
                reachedGoal = False
        fullRepeats = True
        for repeats in keyRepeats:
            if not repeats:
                fullRepeats = False
        if not reachedGoal:
            instructIterator += 1
        if fullRepeats:
            bababooey = 1
            fullRepeats = False
        if fullRepeats and bababooey:
            print(keyRepeats)
            raise Exception(f"finished: {keyRepeats}")
        if instructIterator >= 2**20:
            raise Exception("instructIterator unreasonably high")
        # find every item in keyrow that ends with A
        # put all into list
        # for each iterate through the search process
        # check to see if all are
    return instructIterator + 1


print(partTwo())
