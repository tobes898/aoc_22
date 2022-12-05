# need to grab input
# then of the two pairs break them down into lists
# found condition the smaller of the two numbers (index 0) list
# and that lists index 1 is larger than the other lists than conditon found

inputFile = open('./week_1/inputs/day4_input.txt', 'r')

id_ouput = []
for line in inputFile.readlines():
    cleaned_input = line.strip().split(',')
    output_list = [] 
    output_list.append(cleaned_input[0].split('-'))
    output_list.append(cleaned_input[1].split('-'))
    id_ouput.append(output_list)

assert len(id_ouput) == 1000
print(len(id_ouput))
overlap_count = 0
for line in id_ouput:
    first_id_list = line[0]
    second_id_list = line[1]

    #normal overlap
    #part 1
    if int(first_id_list[0]) <= int(second_id_list[0]) and int(first_id_list[1]) >= int(second_id_list[1]):
        overlap_count +=1
    
    elif int(second_id_list[0]) <= int(first_id_list[0]) and int(second_id_list[1]) >= int(first_id_list[1]):
        overlap_count +=1

    # if the first num is above 2nd range first num but still below 2nd range
    elif int(first_id_list[0]) > int(second_id_list[0]) and int(first_id_list[0]) <= int(second_id_list[1]):
        overlap_count+=1

    elif int(second_id_list[0]) > int(first_id_list[0]) and int(second_id_list[0]) <= int(first_id_list[1]):
        overlap_count+=1



print(overlap_count)

# print(overlap_count)
#example of success 72-72,25-73

#example of failure 31-31,32-40


# def check_lists(first_id_list, second_id_list):
#     if first_id_list[0] < second_id_list[0]:
#         if first_id_list[1] > second_id_list[1]:
#             return True
    
#     elif first_id_list[0] > second_id_list[0]:
#         if second_id_list[1] > first_id_list[1]:
#             return True
#     return False

# # print(overlap_count)
# # 517 too low
# # 596 too high
# assert check_lists(['72', '72'], ['25', '73']) == True

# assert check_lists(['31', '31'], ['32', '40']) == False

# assert check_lists(['72', '73'], ['72', '73']) == False