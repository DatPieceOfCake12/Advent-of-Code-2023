import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    seedLine = lines[1].split()
    seeds = list()
    displacementMap = list()
    for x in range(len(seedLine)):
        seeds.append(int(seedLine[x]))
    for line in lines:
        singleLines = line.strip("\n")
        noSpacelines = singleLines.strip(' ')
        print(repr(line),"\n",repr(singleLines),"\n",repr(noSpacelines),"\n",type(singleLines)," ",type(noSpacelines)," ",(" " in singleLines))
        if (line.strip("\n").strip().isnumeric()):
            print(f"{line} is numeric")
            displacement = line.strip()
            numDisp = list()
            for y in range(len(displacement)):
                numDisp.append(int(displacement[y]))
            displacementMap.append(numDisp)
    return displacementMap

def partTwo():
    print("hi parth")  


# Plan
# Step 1: Get seeds
# Step 2: Iterate through eachline
# Step 3: For each line, if line to string is numeric, then add it to the displacementMap
# Step 4: Once all displacements have been added, iterate through each seed modifying it according to displacement
# Step 5: 

print(f"partone is {partOne()}")
