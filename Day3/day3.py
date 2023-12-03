import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()

def partOne():
    # TODO: fix issue of not fully recognizing full numbers
    # TODO: fix issue of not breaking loop when desired outcome is found and double counting

    symbols = ['+','*','-','=','&','/','@','#','%','$']
    finalValue = 0
    for line in lines:
        currentNum = ""
        for char in line:
            try:
                int(char)
            except ValueError:
                currentNum = ""
            else:
                currentNum += char
                print(f"current num = {currentNum}")
                charIndex = line.index(char)
                lineIndex = lines.index(line)
                print(f"lines adjacent: \n {lines[lineIndex-1]},{lines[lineIndex]},{lines[lineIndex+1]}")
                for x in range(-1,1):
                    checkLine = lines[lineIndex+x]
                    for y in range (-1,1):
                        if(checkLine[charIndex+y] in symbols):
                            finalValue += int(currentNum)
                            break
    return finalValue

print(partOne())

