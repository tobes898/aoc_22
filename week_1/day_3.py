myfile = open('./week_1/inputs/day3_input.txt', 'r')



def common_letter_find(inventory1, inventory2):
    common_letter = ''
    rucksack_inventory_dict = {}
    for letter in inventory1:
        # do first then second
        if letter in rucksack_inventory_dict:
            rucksack_inventory_dict[letter] += 1
        else:
            rucksack_inventory_dict[letter] = 1


        common_letter = ''
        for letter in inventory2:
            if letter in rucksack_inventory_dict:
                common_letter = letter
                break
    return get_priority(common_letter)

def common_letter_find_three_rucksacks(list_of_rucksacks):
    for letter in list_of_rucksacks[0]:
        if letter in list_of_rucksacks[1] and letter in list_of_rucksacks[2]:
            return get_priority(letter)


def get_priority(letter):
    lowercase_list = "abcdefghijklmnopqrstuvwxyz"
    uppercase_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    assert len(lowercase_list) == 26 and len(uppercase_list) == 26
    assert lowercase_list.find('p') + 1 == 16
    assert uppercase_list.find('L') + 27 == 38
    assert lowercase_list.find('P') == -1
    assert uppercase_list.find('p') == -1

    if(letter.isupper()):
        return uppercase_list.find(letter) + 27
    else:
        return lowercase_list.find(letter) + 1
    
rucksacks = []
#clean input
for line in myfile.readlines():
    rucksacks.append(line.strip())

assert len(rucksacks) > 0

# even length need to split each rucksack into the two compartments

split_up_rucksacks = []
# part 1
# for rucksack in rucksacks:
#     cleaned_rucksack = []
#     slice_point = int(len(rucksack) / 2)
#     cleaned_rucksack.append(rucksack[:slice_point])
#     cleaned_rucksack.append(rucksack[slice_point:])
#     split_up_rucksacks.append(cleaned_rucksack)

for i in range(0, len(rucksacks), 3):
    rucksack_group = [rucksacks[i], rucksacks[i+1], rucksacks[i+2]]
    split_up_rucksacks.append(rucksack_group)


assert len(split_up_rucksacks) > 0

sum = 0
for grouping in split_up_rucksacks:
    sum+= common_letter_find_three_rucksacks(grouping)

print(sum)

# part 1
# assert len(split_up_rucksacks[0][0]) == len(split_up_rucksacks[0][1])


# # need to find the common letter in both compartments
# # want to use dictionary 
# common_letter_list = []

# sum = 0
# for compartments in split_up_rucksacks:
#     # common_letter_list.append(common_letter_find(compartments[0],compartments[1]))
#     sum+=common_letter_find(compartments[0],compartments[1])


# assert len(common_letter_list) > 0
# assert common_letter_list[0] > 0

