inputFile = open('./week_2/inputs/day10_small_input.txt')

operations = []
for line in inputFile.readlines():
    operation = line.strip().split(' ')
    operations.append(operation)
register = 1
cycle = 0

for operation in operations:
    cmd = operation[0]
    if cmd == 'noop':
        cycle +=1
        cycle_check(cycle, num)
    else: # op is addx
