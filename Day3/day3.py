import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    # TODO: fix issue of not fully recognizing full numbers
    # TODO: fix issue of not breaking loop when desired outcome is found and double counting

    symbols = ['+','*','-','=','&','/','@','#','%','$']
    finalValue = 0
    skipline = 0
    for line in lines:
        print(f"skip line: {skipline}")
        if(skipline > 0):
            continue
        currentNum = ""
        for charIndex in range(len(line)):
            char = line[charIndex]
            try:
                int(char)
            except ValueError:
                currentNum = ""
            else:
                currentNum = ""
                lineIndex = lines.index(line)
                numIndex = 0
                while(True):
                    try:
                        int(line[charIndex+numIndex])
                    except IndexError:
                        break
                    except ValueError:
                        break
                    else:
                        currentNum += line[charIndex+numIndex]
                        numIndex += 1
                print(f"current num = {currentNum}")

                #print(f"lines adjacent: \n {lines[lineIndex-1]},{lines[lineIndex]},{lines[lineIndex+1]}")
                fullbreak = False
                for x in range(-1,1):
                    if(fullbreak):
                        break
                    checkLine = lines[lineIndex+x]
                    for y in range (len(currentNum)):
                        if(fullbreak):
                            break
                        for z in range(-1,1):
                            if(fullbreak):
                                break
                            if(checkLine[charIndex+y+z] in symbols):
                                print(f"found adjacent value: {currentNum}")
                                finalValue += int(currentNum)
                                skipline = len(currentNum)
                                fullbreak = True
    return finalValue

print(partOne())

