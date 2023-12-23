import os
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    instructions = lines[0].replace("\n","")
    keyRow, leftRow, rightRow = list(), list(), list()
    for line in lines[3:]:
        keyRow.append(line[:3])
        leftRow.append(line[7:10])
        rightRow.append(line[12:15])
    instructIterator = 0
    keyIterator = keyRow.index('AAA')
    reachedGoal = False
    while not reachedGoal:
       currentLine = keyRow[keyIterator]
       print(f"currentLine: {currentLine}")
       print(f"iterator: {instructIterator}")
       print(f'instructor: {instructIterator%(len(instructions))},{instructions[instructIterator%len(instructions)]}')
       match instructions[instructIterator%len(instructions)]:
           case "R":
               currentLine = rightRow[keyIterator] 
           case "L":
               currentLine = leftRow[keyIterator] 
           case _:
               print("error: no value")
       if(currentLine == 'ZZZ'):
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
    instructions = lines[0].replace("\n","")
    keyRow, leftRow, rightRow = list(), list(), list()
    for line in lines[3:]:
        keyRow.append(line[:3])
        leftRow.append(line[7:10])
        rightRow.append(line[12:15])
    instructIterator = 0
    keyIterator = keyRow.index('AAA')
    reachedGoal = False
    while not reachedGoal:
       currentLine = keyRow[keyIterator]
       print(f"currentLine: {currentLine}")
       print(f"iterator: {instructIterator}")
       print(f'instructor: {instructIterator%(len(instructions))},{instructions[instructIterator%len(instructions)]}')
       match instructions[instructIterator%len(instructions)]:
           case "R":
               currentLine = rightRow[keyIterator] 
           case "L":
               currentLine = leftRow[keyIterator] 
           case _:
               print("error: no value")
       if(currentLine == 'ZZZ'):
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


print(partOne())
