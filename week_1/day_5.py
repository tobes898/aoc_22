# [N]     [C]                 [Q]    
# [W]     [J] [L]             [J] [V]
# [F]     [N] [D]     [L]     [S] [W]
# [R] [S] [F] [G]     [R]     [V] [Z]
# [Z] [G] [Q] [C]     [W] [C] [F] [G]
# [S] [Q] [V] [P] [S] [F] [D] [R] [S]
# [M] [P] [R] [Z] [P] [D] [N] [N] [M]
# [D] [W] [W] [F] [T] [H] [Z] [W] [R]
#  1   2   3   4   5   6   7   8   9 
def create_starting_stacks():
    #list of "stacks"
    starting_stacks = []
    starting_stacks.append(['D','M','S','Z','R','F','W','N'])
    starting_stacks.append(['W', 'P', 'Q', 'G', 'S'])
    starting_stacks.append(['W', 'R','V', 'Q', 'F', 'N', 'J', 'C'])
    starting_stacks.append(['F', 'Z', 'P', 'C', 'G', 'D', 'L'])
    starting_stacks.append(['T', 'P', 'S'])
    starting_stacks.append(['H', 'D', 'F', 'W','R','L'])
    starting_stacks.append(['Z', 'N', 'D', 'C'])
    starting_stacks.append(['W','N', 'R', 'F', 'V','S', 'J', 'Q'])
    starting_stacks.append(['R', 'M', 'S', 'G','Z','W','V'])

    assert len(starting_stacks) == 9
    assert len(starting_stacks[0]) == 8
    assert len(starting_stacks[1]) == 5
    assert len(starting_stacks[2]) == 8
    assert len(starting_stacks[3]) == 7
    assert len(starting_stacks[4]) == 3
    assert len(starting_stacks[5]) == 6
    assert len(starting_stacks[6]) == 4
    assert len(starting_stacks[7]) == 8
    assert len(starting_stacks[8]) == 7

    return starting_stacks


def move_crates(n, starting_stack, ending_stack, stacks):
    crate = ''
    #make sure stack is not empty
    if len(stacks[starting_stack]) > 0:
        #part 1
        crate = ''
        crate_pile = []
        counter = 0
        while(counter < n and len(stacks[starting_stack]) > 0):
            crate =  stacks[starting_stack].pop()
            crate_pile.append(crate)
            counter += 1

        while(len(crate_pile) > 0):
            crate = crate_pile.pop()
            stacks[ending_stack].append(crate)

        #part 1
        # crate = stacks[starting_stack].pop()
        # stacks[ending_stack].append(crate)

starting_stacks = create_starting_stacks()

inputFile = open('./week_1/inputs/day5_input.txt', 'r')

print(starting_stacks[0])
for line in inputFile.readlines():
    movements = line.strip().split(' ')
    number = int(movements[1])
    #decrement both by one to make "programming index format"
    starting_pos = int(movements[3]) - 1
    ending_pos = int(movements[5]) - 1

    move_crates(number, starting_pos, ending_pos, starting_stacks)

output = ''

for stack in starting_stacks:
    if len(stack) > 0:
        output += stack.pop()


print(output)


