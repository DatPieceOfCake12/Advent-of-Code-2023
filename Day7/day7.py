import os
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def keepHigher(num1, num2):
    if(num1 > num2):
        return num1
    else:
        return num2

def compareRank(incumbent, challenger):
     # FOR PART 1: charHierarchy = "AKQJT98765432"
    charHierarchy = "AKQT98765432J"
    for index in range(len(incumbent)):
        if (charHierarchy.index(incumbent[index]) > charHierarchy.index(challenger[index])):
            return True
        elif(charHierarchy.index(incumbent[index]) < charHierarchy.index(challenger[index])):
            return False
    return True

def determineJoker(hand):
    highestInd = 0
    for x in set(hand):
        if(hand.count(x) > hand.count(hand[highestInd]) or hand[highestInd] == "J"):
            highestInd = hand.index(x)
    return hand[highestInd]
    # iterate through all unique characters in hand
    # see which one is the most common
    # if len(3), check for fullhouse
    # find return that as joker value
def partition(array, low, high):

	# Choose the rightmost element as pivot
	pivot = array[high]

	# Pointer for greater element
	i = low - 1

	# Traverse through all elements
	# compare each element with pivot
	for j in range(low, high):
		if compareRank(array[j],pivot):
			# If element smaller than pivot is found
			# swap it with the greater element pointed by i
			i = i + 1

			# Swapping element at i with element at j
			(array[i], array[j]) = (array[j], array[i])

	# Swap the pivot element with
	# the greater element specified by i
	(array[i + 1], array[high]) = (array[high], array[i + 1])

	# Return the position from where partition is done
	return i + 1

def quicksort(array, low, high):
	if low < high:

		# Find pivot element such that
		# element smaller than pivot are on the left
		# element greater than pivot are on the right
		pi = partition(array, low, high)

		# Recursive call on the left of pivot
		quicksort(array, low, pi - 1)

		# Recursive call on the right of pivot
		quicksort(array, pi + 1, high)

def partOne():
    totalSum = 0
    pairs = list((list(),list(),list(),list(),list(),list(),list()))
    bids = list()
    hands = list()
    for line in lines:
        power = 0
        hand = line.split()[0].strip()
        bid = int(line.split()[1])
        bids.append(bid)
        hands.append(hand)
        match len(set(hand)):
            case 5:
                power = 0
            case 4:
                power = 1
            case 3:
                for x in set(hand):
                    if(hand.count(x) == 3):
                        power = keepHigher(power, 3)
                    elif(hand.count(x) == 2):
                        power = keepHigher(power, 2)
                # 2 pair & three of a kind
            case 2:
                for x in set(hand):
                    if(hand.count(x) == 4):
                        power = keepHigher(power, 5)
                    elif(hand.count(x) <= 3):
                        power = keepHigher(power, 4)
                # fullhouse & four of kind
            case 1:
                power = 6
            case _:
                print("no length")
        pairs[power].append(hand)
        print(pairs)
    for pair in pairs:
        quicksort(pair, 0, len(pair)-1)
        print(pair)
    iterator = 1
    for pair in pairs:
        for item in pair:
            totalSum += iterator * bids[hands.index(item)]
            iterator += 1
    return totalSum

def partTwo():
    totalSum = 0
    pairs = list((list(),list(),list(),list(),list(),list(),list()))
    bids = list()
    hands = list()
    for line in lines:
        power = 0
        hand = line.split()[0].strip()
        bid = int(line.split()[1])
        bids.append(bid)
        hands.append(hand)
        jokerHand = hand.replace("J",determineJoker(hand))
        match len(set(jokerHand)):
            case 5:
                power = 0
            case 4:
                power = 1
            case 3:
                for x in set(jokerHand):
                    if(hand.count(x) == 3):
                        power = keepHigher(power, 3)
                    elif(hand.count(x) == 2):
                        power = keepHigher(power, 2)
                # 2 pair & three of a kind
            case 2:
                for x in set(jokerHand):
                    if(hand.count(x) == 4):
                        power = keepHigher(power, 5)
                    elif(hand.count(x) <= 3):
                        power = keepHigher(power, 4)
                # fullhouse & four of kind
            case 1:
                power = 6
            case _:
                print("no length")
        pairs[power].append(hand)
    for pair in pairs:
        quicksort(pair, 0, len(pair)-1)
        print(pair)
    iterator = 1
    for pair in pairs:
        for item in pair:
            totalSum += iterator * bids[hands.index(item)]
            iterator += 1
    return totalSum

# Outcome: 1 star

print(partTwo())
