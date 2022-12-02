# add code to read file

# blank line = end of input - need to increment to next elf
# on space take sum and store in list

inputFile = open('inputs/day1_input.txt', 'r')
inputList = []
for line in inputFile.readlines():
    inputList.append(line.strip())

elf_calories = []
sum = 0
output_list = []
counter = 0
for line in inputList:
    if line == '':
        output_list.append(sum)
        sum = 0
    else:
        sum += int(line)


max_value = -1
for line in output_list:
    if max_value < line:
        max_value = line
# print(output_list[0])

# print(max_value)

output_list.sort(reverse=True)
assert output_list[0] == 70720

print(output_list[0]+output_list[1]+output_list[2])
# assert output_list[0] == 43554