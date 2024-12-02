def get_lists(content):
    right_list = []
    left_list = []

    for line in content.splitlines():
        pair_list = line.split("   ")
        if len(pair_list) == 2:
            right_list.append(pair_list[0])
            left_list.append(pair_list[1])
    
    return left_list, right_list

def part_1(content):
    """
    Process the content by splitting lines, sorting, converting to integers,
    and calculating the difference between corresponding elements.
    """

    left_list, right_list = get_lists(content)

    left_list.sort()
    right_list.sort()

    left_list = [int(x) for x in left_list]

    right_list = [int(x) for x in right_list]

    difference = [abs(left_list[i] - right_list[i]) for i in range(len(left_list))]

    return sum(difference)

with open('input.txt', 'r') as file:
    content = file.read()
print("Part 1")
result = part_1(content)
print(result)

def part_2(content):
    left_list, right_list = get_lists(content)
    
    left_list = [int(x) for x in left_list]
    right_list = [int(x) for x in right_list]



    similarity_score = 0
    for i in range(len(left_list)):
        similarity_score += left_list[i] * right_list.count(left_list[i])

    return similarity_score


print("Part 2")
part_2_res = part_2(content)
print(part_2_res)
