def part2():
    lst = [int(num) for num in input().split(',')]
    for noun in range(100):
        new_lst = [x for x in lst]
        for verb in range(100):
            new_lst[1] = noun
            new_lst[2] = verb
            if part1(new_lst) == 19690720:
                return 100 * noun + verb
        

def part1():
    lst = [int(num) for num in input().split(',')]
    for i in range(0, len(lst), 4):
        opcode = new_lst[i]
        if opcode == 1:
            new_lst[new_lst[i + 3]] = new_lst[new_lst[i + 1]] + new_lst[new_lst[i + 2]]
        elif opcode == 2:
            new_lst[new_lst[i + 3]] = new_lst[new_lst[i + 1]] * new_lst[new_lst[i + 2]]
        else:
            break
    return new_lst[0]


print(part1())
print(part2())