import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()


def partOne():
    idsum = 0
    for line in lines:
        print("new round")
        game = line.split(":")
        rounds = game[1].split(";")
        isSafe = True
        for x in rounds:
            cubes = x.split(",")
            print("cubes: ")
            print(cubes)
            for cube in cubes:
                number = int(cube[:3]) 
                if((number <= 12 and "red" in cube)or(number <= 13 and "green" in cube)or(number <= 14 and "blue" in cube)):
                    print(cube + " is safe")
                else:
                    print(cube + " is unsafe")
                    isSafe = False
        if(isSafe):
            fullid = game[0]
            idsum += int(fullid[5:])
            print("idsum is "+ (fullid[5:]))
    print(idsum)

def partTwo():
    #TODO: like everything lmao
    fullTotal = 0
    for line in lines:
        print("new round")
        game = line.split(":")
        rounds = game[1].split(";")
        maxRed = 0
        maxBlue = 0
        maxGreen = 0
        for x in rounds:
            cubes = x.split(",")
            print("cubes: ")
            print(cubes)
            for cube in cubes:
                number = int(cube[:3]) 
                if("red" in cube):
                    if(number > maxRed):
                        maxRed = number
                if("blue" in cube):
                    if(number > maxBlue):
                        maxBlue = number
                if("green" in cube):
                    if(number > maxGreen):
                        maxGreen = number
        print("r,g,b")
        print(maxRed, maxGreen, maxBlue)
        roundTotal = int(maxGreen) * int(maxRed) * int(maxBlue)
        fullTotal += roundTotal
    return fullTotal

print(partTwo())
