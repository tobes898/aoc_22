
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

def calc_H_movement(grid, movement, current_pos_H, current_pos_T):
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
            count = calc_T_movement(grid,current_pos_T,current_pos_H, count)

    # L -> x - n
    if direction == 'L':
        new_x_pos = x_pos - num

        while x_pos > new_x_pos:
            x_pos -= 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            count = calc_T_movement(grid,current_pos_T,current_pos_H, count)



    # U -> y - n
    if direction == 'U':
        new_y_pos = y_pos - num

        while y_pos > new_y_pos:
            y_pos -= 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            count =calc_T_movement(grid,current_pos_T,current_pos_H, count)



    # D -> y + n
    if direction == 'D':
        new_y_pos = y_pos + num

        while y_pos < new_y_pos:
            y_pos += 1
            move_H(grid, x_pos, y_pos, current_pos_H)
            count =calc_T_movement(grid,current_pos_T,current_pos_H, count)

    print(count)

def move_T_left_right(grid, current_pos_T, x_diff):
    new_x_pos = current_pos_T[0]
    if x_diff < -1:
        new_x_pos += 1
    else:
        new_x_pos -= 1

    # update grid with new T location
    grid[current_pos_T[1]][new_x_pos] = 'T'
    # update visited
    # movement_tracker[current_pos_T[1]][new_x_pos] = '#'
    # update grid to set prev location back to .
    grid[current_pos_T[1]][current_pos_T[0]] = '.'
    current_pos_T[0] = new_x_pos

def move_T_up_down(grid, current_pos_T, y_diff):
    new_y_pos = current_pos_T[1]
    if y_diff < -1:
        new_y_pos += 1
    else:
        new_y_pos -= 1
    
    grid[new_y_pos][current_pos_T[0]] = 'T'
    
    # movement_tracker[new_y_pos][current_pos_T[0]] = '#'

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

def move_T_diagonal(grid, current_pos_T, x_difference, y_difference):
    new_x_pos = current_pos_T[0]
    new_y_pos = current_pos_T[1]
    if x_difference == -1:
        new_x_pos +=1
        if y_difference < -1:
            new_y_pos += 1
        else:
            new_y_pos -= 1
    else:
        new_x_pos -= 1
        if y_difference < -1:
            new_y_pos += 1
        else:
            new_y_pos -= 1

    grid[new_y_pos][new_x_pos] = 'T'
    # movement_tracker[new_y_pos][new_x_pos] = '#'
    grid[current_pos_T[1]][current_pos_T[0]] = '.'
    current_pos_T[0] = new_x_pos
    current_pos_T[1] = new_y_pos



def calc_T_movement(grid, current_pos_T, current_pos_H, count):
    count += 1

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
        move_T_left_right(grid, current_pos_T, x_difference)
    # adjust just y
    elif abs(y_difference) > 1 and x_difference == 0:
        move_T_up_down(grid, current_pos_T, y_difference)

    elif abs(x_difference) == 1 and abs(y_difference) > 1:
        move_T_diagonal(grid, current_pos_T, x_difference, y_difference)

    print('---------')
    print_grid(grid)
    print('---------')
    print(current_pos_T)
    print(current_pos_H)
    return count

inputFile = open('./week_2/inputs/day9_even_smaller_input.txt', 'r')

movement = []
for line in inputFile.readlines():
    movement.append(line.strip().split(' '))

assert len(movement) > 0

#step by step move head and then check what movement tail needs to stay correct

# create grid
x_len = 6
y_len = 5

grid = []
global movement_tracker
movement_tracker = []



for i in range(0, y_len):
    row = []
    for j in range(0, x_len):
        row.append('.')
    grid.append(row)
    movement_tracker.append(row)

# start is bottom left of grid so (0, len(y) -1)
current_pos_H = [0, y_len-1]
current_pos_T = [0, y_len-1]
# movement_tracker[0][y_len-1] = 's'
grid[y_len-1][0] = 'H'

for move in movement:
 
    calc_H_movement(grid, move, current_pos_H, current_pos_T)
    # calc_T_movement(grid, current_pos_T, current_pos_H)



print_grid(grid)
# print_grid(movement_tracker)
# print(count)
#if difference between T and H is 2 then T needs to move closer to H
#need to execute each move individually

