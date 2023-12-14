import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    finalPoints = 0
    for line in lines:
        fullCardNums = line.split(":")
        numSections = fullCardNums[1].split('|')
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
    # TODO: Fix index errors
    finalPoints = 0
    copyCount = [1] * 187
    for line in lines:
        fullCardNums = line.split(":")
        idSplit = fullCardNums[0].split()
        id = int(idSplit[1])
        print(f" Id: {id}")
        numSections = fullCardNums[1].split('|')
        winningNums = numSections[0].split()
        cardNums = numSections[1].split()
        #print(f"Full card Nums: {fullCardNums}")
        #print(f"winning: {winningNums} \n cardnums: {cardNums}")
        amountWinningNums = 0
        for x in cardNums:
            if(x in winningNums):
                amountWinningNums += 1
                print(f"winning#: {amountWinningNums}")
                print(f"copies {id-1} : {copyCount[id-1]}")
        for y in range(amountWinningNums):
            print(id+y)
            copyCount[id+y] += copyCount[id-1]
            print(f" id to copycount {id}:{copyCount[id-1]}")
    for a in range(187):
        finalPoints += copyCount[a]
        print(f"finalPoints {a}: {finalPoints}")
    return finalPoints


# Final outcome: 2 stars
print(partTwo())
