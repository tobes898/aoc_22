
inputFile = open("./week_1/inputs/day6_input.txt", "r")
inputLine = inputFile.readlines()
inputFile.close()

assert len(inputLine) == 1

def evaluate_list (charList):
    for i in range(0, len(charList)):
        for j in range(i+1, len(charList)):
            if charList[i] == charList[j]:
                return False
    return True


charList = []
charDict = {}
counter = 0
#part 1
# distinct_character = 4
distinct_character = 14
for c in inputLine[0]:
    
    if len(charList) == distinct_character:
        if(evaluate_list(charList)):
            break
        else:
            charList.pop(0)

    charList.append(c)
    counter += 1
print(counter)
assert len(charList) > 1
