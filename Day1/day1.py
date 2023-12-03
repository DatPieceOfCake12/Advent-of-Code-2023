import os;
dirname = os.path.dirname(__file__)
input = open(os.path.join(dirname, "input.txt"))
lines = input.readlines()



numberwords = {"one" : 1,"two" : 2,"three" : 3,"four" : 4,"five" : 5,"six" : 6,"seven" : 7,"eight" : 8,"nine" : 9}
numberwordsarray = ["one","two" ,"three","four","five","six","seven","eight" ,"nine"]
charsum = [0,0]
endsum = 0

def checkforWord(checkNumWord):
        for x in numberwordsarray:
            if(x in checkNumWord):
                print('found:' + checkNumWord)
                return numberwords[x]
            elif(x in checkNumWord[::-1]):
                print('found:' + checkNumWord)
                return numberwords[x]
            else:
                print(checkNumWord)

def checkForInt(line):
    checkNumWord = ""
    for char in line:
        try:
            int(char)
        except ValueError:
            checkNumWord += char
            if(checkforWord(checkNumWord) == None):
                pass
            else:
                return checkforWord(checkNumWord)
        else:
            return int(char)


for line in lines:
    charsum[0] = checkForInt(line)
    charsum[1] = checkForInt(line[::-1])
    print("Should be: "+str(charsum[0])+", " + str(charsum[1]))
    print("is :"+str(charsum[0]+charsum[1]))
    endsum += int(str(charsum[0])+str(charsum[1]))

print(endsum)
    

    
# End Result: 2/2 Stars