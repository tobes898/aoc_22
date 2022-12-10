
def print_grid(grid):
    for i in range(0, len(grid)):
        printed_str = ''
        for j in range(0, len(grid[0])):
            printed_str += grid[i][j]
        print(printed_str)

def move_H(grid, x_pos, y_pos, current_pos_H):
    grid[y_pos][x_pos] = 'H'
    grid[current_pos_H[1]][current_pos_H[0]] = '.'
    current_pos_H[0] = x_pos
    current_pos_H[1] = y_pos

def calc_H_movement(grid, movement, current_pos_H, current_pos_T, list_of_tails):
    direction = movement[0].upper()
    num = int(movement[1])
    x_pos = current_pos_H[0]
    y_pos = current_pos_H[1]
    new_x_pos = -1
    new_y_pos = -1
    count = 0
    # R -> x + n
    if direction == 'R':
        new_x_pos = x_pos+num

        while x_pos < new_x_pos:
            x_pos += 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            calc_T_movement(grid,list_of_tails[0],current_pos_H, False)
            for i in range(1, len(list_of_tails)):
                if i == len(list_of_tails) - 1:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], True)
                else:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], False)


    # L -> x - n
    if direction == 'L':
        new_x_pos = x_pos - num

        while x_pos > new_x_pos:
            x_pos -= 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            calc_T_movement(grid,list_of_tails[0],current_pos_H, False)
            for i in range(1, len(list_of_tails)):
                if i == len(list_of_tails) - 1:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], True)
                else:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], False)



    # U -> y - n
    if direction == 'U':
        new_y_pos = y_pos - num

        while y_pos > new_y_pos:
            y_pos -= 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            # move list 
            calc_T_movement(grid,list_of_tails[0],current_pos_H, False)
            for i in range(1, len(list_of_tails)):
                if i == len(list_of_tails) - 1:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], True)
                else:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], False)




    # D -> y + n
    if direction == 'D':
        new_y_pos = y_pos + num

        while y_pos < new_y_pos:
            y_pos += 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            calc_T_movement(grid,list_of_tails[0],current_pos_H, False)
            for i in range(1, len(list_of_tails)):
                if i == len(list_of_tails) - 1:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], True)
                else:
                    calc_T_movement(grid, list_of_tails[i],list_of_tails[i-1], False)


    # print(count)

def move_T_left_right(grid, current_pos_T, x_diff, track):
    new_x_pos = current_pos_T[0]
    if x_diff < -1:
        new_x_pos += 1
    else:
        new_x_pos -= 1

    # update grid with new T location
    grid[current_pos_T[1]][new_x_pos] = 'T'
    # update visited
    if track:
        movement_tracker[current_pos_T[1]][new_x_pos] = '#'
    # update grid to set prev location back to .
    grid[current_pos_T[1]][current_pos_T[0]] = '.'
    current_pos_T[0] = new_x_pos

def move_T_up_down(grid, current_pos_T, y_diff, track):
    new_y_pos = current_pos_T[1]
    if y_diff < -1:
        new_y_pos += 1
    else:
        new_y_pos -= 1
    
    grid[new_y_pos][current_pos_T[0]] = 'T'
    
    if track:
        movement_tracker[new_y_pos][current_pos_T[0]] = '#'

    grid[current_pos_T[1]][current_pos_T[0]] = '.'
    current_pos_T[1] = new_y_pos


#top right +1 x & -1 y
# diff -1x & +2 y

#bottom right +1 x & +1 y
# diff -1x & -2y

#top left -1 x & -1 y
#diff +1x & +2y

#bottom left -1 x & +1y
#diff +1x & -2y

def move_T_diagonal(grid, current_pos_T, x_difference, y_difference, track):
    # need to add more to x difference here 
    new_x_pos = current_pos_T[0]
    new_y_pos = current_pos_T[1]
    if x_difference == -1:
        new_x_pos +=1
        if y_difference < -1:
            new_y_pos += 1
        else:
            new_y_pos -= 1
    elif x_difference == 1:
        new_x_pos -= 1
        if y_difference < -1:
            new_y_pos += 1
        else:
            new_y_pos -= 1
    
    elif y_difference == -1:
        new_y_pos+=1
        if x_difference < -1:
            new_x_pos += 1
        else:
            new_x_pos -= 1
    elif y_difference == 1:
        new_y_pos -= 1
        if x_difference < -1:
            new_x_pos += 1
        else:
            new_x_pos -= 1

    grid[new_y_pos][new_x_pos] = 'T'
    if track:
        movement_tracker[new_y_pos][new_x_pos] = '#'
    grid[current_pos_T[1]][current_pos_T[0]] = '.'
    current_pos_T[0] = new_x_pos
    current_pos_T[1] = new_y_pos



def calc_T_movement(grid, current_pos_T, current_pos_H, track):
    # count += 1

    # note for tommorrow - issue is when index is 0
    # likely need increment everything by one when calculating difference
    # need to make sure difference isn't explicitly used anywhere when setting
    # grid
    x_difference = current_pos_T[0] - current_pos_H[0]
    y_difference = current_pos_T[1] - current_pos_H[1]
    # new_x_pos = current_pos_T[0]
    # new_y_pos = current_pos_T[1]
    #if negative num need to add
    #if positive num need to subtract
    # both x and y have a difference
    # just x
    # just y

    # adjust both (ie. diagonal movement)
    # adjust just x
    if abs(x_difference) > 1 and y_difference == 0:
        move_T_left_right(grid, current_pos_T, x_difference, track)
    # adjust just y
    elif abs(y_difference) > 1 and x_difference == 0:
        move_T_up_down(grid, current_pos_T, y_difference, track)

    elif (abs(x_difference) == 1 or abs(y_difference) == 1) and (abs(y_difference) > 1 or abs(x_difference) > 1):
        move_T_diagonal(grid, current_pos_T, x_difference, y_difference, track)

    # print('---------')
    # print_grid(grid)
    # # print('---------')
    # print(current_pos_T)
    # print(current_pos_H)
    # return count

inputFile = open('./week_2/inputs/day9_input.txt', 'r')

movement = []
for line in inputFile.readlines():
    movement.append(line.strip().split(' '))

assert len(movement) > 0

#step by step move head and then check what movement tail needs to stay correct

# create grid
x_len = 1000
y_len = 1000

grid = []
global movement_tracker
movement_tracker = []



for i in range(0, y_len):
    row = []
    for j in range(0, x_len):
        row.append('.')
    grid.append(row)


for i in range(0, y_len):
    row = []
    for j in range(0, x_len):
        row.append('.')
    movement_tracker.append(row)


starting_x = int(x_len / 500) -1
starting_y = int(y_len / 500) - 1
starting_x = 15
starting_y = 11
# start is bottom left of grid so (0, len(y) -1)
rope_parts = []
amount_of_parts = 10

for i in range(0, amount_of_parts):
    part = [starting_x, starting_y]
    rope_parts.append(part)

# need way to only do visit grid on last tail? or grid for each tail
current_pos_H = [starting_x, starting_y]
# current_pos_T = [starting_x, starting_y]
# movement_tracker[0][y_len-1] = 's'
grid[starting_y][starting_x] = 'H'

movement_tracker[starting_y][starting_x] = 's'
for move in movement:
 
    calc_H_movement(grid, move, current_pos_H, rope_parts[0], rope_parts)
    # calc_T_movement(grid, current_pos_T, current_pos_H)



# print_grid(grid)
# print_grid(movement_tracker)
# print_grid(movement_tracker)
# print(count)
#if difference between T and H is 2 then T needs to move closer to H
#need to execute each move individually
#420
#451 too low
#510
count = 0
for i in range(0, len(movement_tracker)):
    for j in range(0, len(movement_tracker[0])):
        if movement_tracker[i][j] == '#' or movement_tracker[i][j] == 's':
            count += 1

print(count)