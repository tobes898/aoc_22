inputFile = open('./week_2/inputs/day10_input.txt')

operations = []
for line in inputFile.readlines():
    operation = line.strip().split(' ')
    operations.append(operation)
register = 1
cycle = 0

def make_screen():
    screen = []
    for i in range(0,6):
        pixel_row =[]
        for j in range(0,40):
            pixel_row.append('.')
        screen.append(pixel_row)
    return screen

def print_screen(screen):
    for i in range(0, 6):
        screen_line =''
        for j in range(0,40):
            screen_line += screen[i][j]
        print(screen_line)
            

register_status = []
# print(operations)
screen = make_screen()
print_screen(screen)
cycle_max = 240
op_complete = -1
row = 0
row_loc = 0
current_op = ['noop']
while cycle < cycle_max:
    if op_complete <= cycle:
        if current_op[0] == 'addx':
            register += int(current_op[1])
        if len(operations) == 0:
            break
        current_op = operations.pop(0)
        if current_op[0] == 'addx':
            op_complete = cycle + 2
    
    if cycle % 40 == 0 and cycle != 0:
        row +=1
        row_loc = 0
    try:
        if row_loc == register or row_loc == (register - 1) or row_loc == register + 1:
            screen[row][row_loc] = '#'
    except IndexError:
        exit(0)
    row_loc += 1
    cycle += 1
    register_status.append(register)
    # print(cycle)

st_n = 20
sum = 0
register_status.sort()
print(register_status[len(register_status)-1]) # need max line of 38
# check_list = []
# check_list.append(20 * register_status[st_n -1])
for i in range(st_n, 221, 40):
    # print(i)
    sum += (i * register_status[i-1])
    # check_list.append(i * register_status[i-1])


# print(check_list)
print_screen(screen)
print(sum)