class Monkey(object):

    def __init__(self, items, x, op, y, num_check, on_success, on_failure):
        self.items = items
        self.x = x
        self.op = op
        self.y = y
        self.num_check = num_check
        self.on_success = on_success
        self.on_failure = on_failure
        self.num_inspect = 0

    def run_op(self, item):
        val_1 = self.x
        if val_1 == 'old':
            val_1 = item
        val_2 = self.y
        if val_2 == 'old':
            val_2 = item

        if self.op == '+':
            return val_1 + val_2
        elif self.op == '-':
            return val_1 - val_2
        elif self.op == '*':
            return val_1 * val_2
        elif self.op == '/':
            return val_1 / val_2

    def make_decision(self, item):
        if self.run_op(item) % self.num_check == 0:
            return self.on_success
        else:
            return self.on_failure


        


# create Monkeys based on input

list_of_monkeys = []
list_of_monkeys.append(Monkey([77, 69, 76, 77, 50, 58], 'old', '*', 11,5,1,5))
list_of_monkeys.append(Monkey([75, 70, 82, 83, 96, 64, 62], 'old', '+', 8,17,5,6))
list_of_monkeys.append(Monkey([53], 'old', '*', 3,2,0,7))
list_of_monkeys.append(Monkey([85, 64, 93, 64, 99], 'old', '+', 4,7,7,2))
list_of_monkeys.append(Monkey([61, 92, 71], 'old', '*', 'old',3,2,3))
list_of_monkeys.append(Monkey([79, 73, 50, 90], 'old', '+', 2,11,4,6))
list_of_monkeys.append(Monkey([50, 89], 'old', '+', 3,13,4,3))
list_of_monkeys.append(Monkey([83, 56, 64, 58, 93, 91, 56, 65], 'old', '+', 5,19,1,0))


assert len(list_of_monkeys) == 8
for i in range(0, 20):
    for monkey in list_of_monkeys:
        for item in monkey.items:
            monkey.num_inspect +=1
            index = monkey.make_decision(item)
            list_of_monkeys[index].items.append(monkey.items.pop(0))

sum = 1
inspect_list = []
for monkey in list_of_monkeys:
    inspect_list.append(monkey.num_inspect)

inspect_list.sort()
x = len(inspect_list)
print(inspect_list[x-1] * inspect_list[x-2])

# print(sum)