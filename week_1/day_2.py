# first column is opponent
# 2nd column is what you play

# A = Rock | B = Paper | C = Scissors
# X = Rock | Y = Paper | Z = Scissors
# Rock = 1 | Paper = 2 | Scissors = 3
# Lost = 0 | Draw = 3 | Win = 6

# part 1
#A beats C
#B beats A
#C beats B



# part 2
# x = loser

#translate to common id
def resolve_score(move):
    if move == 'A':
        return 1
    elif move == 'B':
        return 2
    else:
        return 3

arr_of_output = []
loser_dict = {'A':'C', 'B':'A', 'C':'B'}
winner_dict = {'C':'A', 'A':'B', 'B':'C'}
inputFile = open('inputs/day2_input.txt', 'r')


sum = 0
for line in inputFile.readlines():
    
    output = line.split()
    if output[1] == 'X':
        sum += resolve_score(loser_dict[output[0]])
    elif output[1] == 'Y':
        sum += 3
        sum += resolve_score(output[0])
    else:
        sum += 6
        sum += resolve_score(winner_dict[output[0]])

    # if output[1] == output[0]:
    #     sum += 3
    
    # elif output[1] == 'A' and output[0] == 'C':
    #     sum += 6
    
    # elif output[1] == 'B' and output[0] == 'A':
    #     sum += 6

    # elif output[1] == 'C' and output[0] == 'B':
    #     sum += 6
    arr_of_output.append(output)



assert len(arr_of_output) > 0
print(arr_of_output[0])

print(sum)