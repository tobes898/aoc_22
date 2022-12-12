inputFile = open('./week_2/inputs/day12_sample_input.txt')

grid = []
for line in inputFile.readlines():
    temp = []
    for c in line.strip():
        temp.append(c)

    grid.append(temp)

alphabet = 'abcdefghijklmnopqrstuvwxyz'
alpha_list = []
for c in alphabet:
    alpha_list.append(c)
for row in grid:
    print(row)

print(len(alpha_list))



def movable (x, x_index):
    if x == 'a':
        return [0, 1]

    if x == 'z':
        return[25, 26]

    return [x_index, x_index-1, x_index+1]

