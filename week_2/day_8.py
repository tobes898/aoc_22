inputFile = open('./week_2/inputs/day8_input.txt', 'r')

output_grid = []
for line in inputFile.readlines():
    line = line.strip()
    line_of_trees = []
    for tree in line:
        line_of_trees.append(tree)
    output_grid.append(line_of_trees)


visible_list = []
scenic_score_list = []
for i in range (0, len(output_grid[0])):
    temp_list = []
    temp_list2 = []
    for j in range(0, len(output_grid)):
        temp_list.append(False)
        temp_list2.append(1)
        # visible_list[i][j] = False
    visible_list.append(temp_list)
    scenic_score_list.append(temp_list2)


assert len(visible_list) == len(output_grid)
assert len(visible_list[0]) == len(output_grid[0])


# set perimeter all to True
for i in range(0, len(output_grid[0])):
    for j in range(0, len(output_grid)):
        if (i == 0 or i == len(output_grid[0]) - 1) or (j == 0 or j == len(output_grid) - 1): # x-axis
            visible_list[i][j] = True


def compare_coordinates(pt_1, pt_2):
    if pt_1 > pt_2:
        return True
    return False

def check_top(grid, x, y):
    # if visible_list[x][y] == True:
    #     return
    scenic_count = 1
    new_y = y - 1
    while(check_y_edge(new_y, len(grid) - 1)):
        if(compare_coordinates(grid[x][y], grid[x][new_y])):
            new_y -= 1
            scenic_count += 1
        else:
            scenic_score_list[x][y] *= scenic_count
            return
    
    if compare_coordinates(grid[x][y], grid[x][new_y]):
        visible_list[x][y] = True
    scenic_score_list[x][y] *= scenic_count

def check_bottom(grid, x, y):
    # if visible_list[x][y] == True:
    #     return
    scenic_count = 1
    new_y = y + 1
    while(check_y_edge(new_y, len(grid) - 1)):
        if(compare_coordinates(grid[x][y], grid[x][new_y])):
            new_y += 1
            scenic_count += 1
        else:
            scenic_score_list[x][y] *= scenic_count
            return
        
    if compare_coordinates(grid[x][y], grid[x][new_y]):
        visible_list[x][y] = True
    scenic_score_list[x][y] *= scenic_count

def check_left(grid, x, y):
    # if visible_list[x][y] == True:
    #     return
    scenic_count = 1
    new_x = x - 1
    while(check_x_edge(new_x, len(grid[0])-1)):
        if(compare_coordinates(grid[x][y], grid[new_x][y])):
            new_x -= 1
            scenic_count += 1
        else:
            scenic_score_list[x][y] *= scenic_count
            return
    
    if compare_coordinates(grid[x][y], grid[new_x][y]):
        visible_list[x][y] = True
    scenic_score_list[x][y] *= scenic_count

def check_right(grid, x, y):
    # if visible_list[x][y] == True:
    #     return
    scenic_count = 1
    new_x = x + 1
    while(check_x_edge(new_x, len(grid[0])-1)):
        if(compare_coordinates(grid[x][y], grid[new_x][y])):
            new_x += 1
            scenic_count += 1
        else:
            scenic_score_list[x][y] *= scenic_count
            return
    
    if compare_coordinates(grid[x][y], grid[new_x][y]):
        visible_list[x][y] = True
    scenic_score_list[x][y] *= scenic_count
def check_y_edge(y, max_y):
    if y == 0 or y == max_y:
        return False
    return True

def check_x_edge(x, max_x):
    if x == 0 or x == max_x:
        return False
    return True


for i in range(1, len(output_grid[0]) - 1):
    for j in range(1, len(output_grid) - 1):
        check_top(output_grid, i, j)
        check_bottom(output_grid, i, j)
        check_right(output_grid, i, j)
        check_left(output_grid, i, j)

count = 0
max = -1
for i in range(0, len(output_grid[0])):
    for j in range(0, len(output_grid)):
        if visible_list[i][j]:
            count += 1
        if scenic_score_list[i][j] > max:
            max = scenic_score_list[i][j]
print(count)
print(max)
# print(scenic_score_list)