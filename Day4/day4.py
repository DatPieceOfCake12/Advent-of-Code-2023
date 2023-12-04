import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    finalPoints = 0
    for line in lines:
        fullCardNums = line.split(":")
        numSections = fullCardNums[1].split('|')
        # can I seperate a string by spaces?
        winningNums = numSections[0].split()
        cardNums = numSections[1].split()
        print(f"Full card Nums: {fullCardNums}")
        print(f"winning: {winningNums} \n cardnums: {cardNums}")
        amountWinningNums = 0
        for x in cardNums:
            if(x in winningNums):
                amountWinningNums += 1
        print(f"{amountWinningNums} therefore added value is {2**(amountWinningNums-1)}")
        if(amountWinningNums != 0):
            finalPoints += 2**(amountWinningNums-1)
    return finalPoints

def partTwo():
    finalPoints = 0
    copyCount = [1] * 80
    for line in lines:
        fullCardNums = line.split(":")
        idSplit = fullCardNums[0].split()
        id = int(idSplit[1])
        numSections = fullCardNums[1].split('|')
        # can I seperate a string by spaces?
        winningNums = numSections[0].split()
        cardNums = numSections[1].split()
        print(f"Full card Nums: {fullCardNums}")
        print(f"winning: {winningNums} \n cardnums: {cardNums}")
        amountWinningNums = 0
        for x in cardNums:
            if(x in winningNums):
                amountWinningNums += 1
        for y in range(amountWinningNums):
            for z in range(copyCount[id]):
                copyCount[id+y-1]+= 1
    return finalPoints

print(partTwo())
