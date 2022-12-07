# cd {dir} - create new node with current node set to its parent
# ls - add following dir and files as new nodes that a children of current node
# cd .. - set current node back to parent node  
class Node(object):
    def __init__(self, parent=None, name='',children={}, data_size=0, dir_flag=False):
        self.parent = parent
        self.children = children
        self.data_size = 0
        self.dir_flag = dir_flag
        self.name = name
    def print_node(self):
        print('dir:' + str(self.name)+ ' Parent:' + str(self.parent.name))

    def add_to_children(self, child):
        self.children.append(child)


# splits cmd into ways to process it
# list_flag is used to signify needing to add the following line(s) output as children
# of current node. Always set to false at execute cmd

global my_list
my_list = []
global target_number
target_number = 100000
my_dict = {}
def change_directory(node_ptr, name_of_dir):
    #use existing node
    if name_of_dir == '..':
        #part 2
        if node_ptr.name not in my_dict:
            my_dict[node_ptr.name] = node_ptr.data_size
        # end of part 2
        if node_ptr.data_size <= target_number:
            my_list.append(node_ptr)
        node_ptr.parent.data_size += int(node_ptr.data_size)
        return node_ptr.parent
    elif node_ptr != None and name_of_dir in node_ptr.children:
        return node_ptr.children[name_of_dir]
    elif node_ptr == None:
        temp_node = Node(name=str(name_of_dir), children={}, parent=None, dir_flag=True)
        return temp_node
    else:
        temp_node = Node(name=str(name_of_dir), children={}, parent=node_ptr, dir_flag=True)
        return temp_node

def add_child_from_ls(node_ptr, item):
    if(item[0] == 'dir'):
        temp_node = Node(name=str(item[1]), parent=node_ptr, children={}, dir_flag=True)
        temp_dict = node_ptr.children
        temp_dict[str(item[1])] = temp_node
        node_ptr.children = temp_dict
    else:
        temp_node = Node(name=str(item[1]), parent=node_ptr, children={}, data_size=item[0], dir_flag=True)
        temp_dict = node_ptr.children
        temp_dict[str(item[1])] = temp_node
        node_ptr.children = temp_dict
        node_ptr.data_size += int(item[0])
    return node_ptr

def execute_command(line, node_ptr):
    breakdown_cmd = line.split(' ')
    if(breakdown_cmd[1] == 'cd'):
        node_ptr = change_directory(node_ptr, breakdown_cmd[2])
    elif (breakdown_cmd[1] != 'ls'):
        node_ptr = add_child_from_ls(node_ptr, breakdown_cmd)
    return node_ptr




inputFile = open('./week_1/inputs/day7_input.txt', 'r')

std_input_output = []
for line in inputFile.readlines():
    std_input_output.append(line.strip())

assert len(std_input_output) > 0

node_ptr = None
for line in std_input_output:
    node_ptr = execute_command(line, node_ptr)

while(node_ptr.name != '/'):
    if node_ptr.name not in my_dict:
            my_dict[node_ptr.name] = node_ptr.data_size
    if node_ptr.data_size <= target_number:
            my_list.append(node_ptr)
    node_ptr.parent.data_size += int(node_ptr.data_size)
    node_ptr = node_ptr.parent


# print(my_dict.values())




# return to root
# print(node_ptr.data_size)
# print(my_list)
sum = 0
for node in my_list:
    sum += node.data_size

print(sum)
starting_node = None
temp_node = node_ptr
while(temp_node is not None):
    starting_node = temp_node
    temp_node = temp_node.parent

size_list = list(my_dict.values())
size_list.sort()
print(size_list)
total_disk_size = 70000000
current_used_disk = starting_node.data_size
target_deletion_size = 30000000 - (total_disk_size - current_used_disk)
print(target_deletion_size)
lowest_possible_size = -1

for dir_size in size_list:
    if dir_size >= target_deletion_size:
        lowest_possible_size = dir_size
        break

print(lowest_possible_size)











# test = Node('root', None, 'root')
# test.print_node()