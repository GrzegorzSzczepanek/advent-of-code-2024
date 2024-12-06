from pprint import pprint


def read_file(filepath: str) -> str:
    return open(filepath, "r").read().strip()


def transpose_2d(lst: list):
    new_lst = []
    for i in range(len(lst[0])):
        row = []
        for item in lst:
            row.append(item[i])
        new_lst.append("".join(row))

    return new_lst


def pad_row(row: list):
    while len(row) < 6:
        row.append(None)
    return row


def diagonals_to_rows(puzzle: list):
    """
    It works under assumption that list has square n x n shape.
    """
    new_lst = []

    for i in range(0, len(puzzle[0])):
        diagonal = []
        for j in range(i, len(puzzle[0])):
            if i != 0:
                if j < len(puzzle[0]) - 1:
                    diagonal.append(puzzle[j][j + 1])
                else:
                    break
            else:
                diagonal.append(puzzle[j][j])

        new_lst.append(pad_row(diagonal))

    for i in range(len(puzzle[0])):
        diagonal = []
        for j in range(i + 1):
            if i - j >= 0:
                diagonal.append(puzzle[j][i - j])
        new_lst.append(pad_row(diagonal))
    # pprint(new_lst)

    # print(new_lst)
    return new_lst


def check_horizontal(puzzle: list[str]) -> int:
    count = 0

    for line in puzzle:
        # print(line)
        for i in range(len(line) - 3):
            if line[i : i + 4] in ["XMAS", "SAMX"]:
                count += 1

    # print("\n".join(puzzle), "\n\n")
    print(count)

    return count


def check_vertical(puzzle: list[str]) -> int:
    count = 0
    p_transposed = transpose_2d(puzzle)

    count = check_horizontal(p_transposed)

    return count


def part1(input_file: str) -> int:
    xmas_count = 0

    puzzle = read_file(input_file).split("\n")
    # xmas_count += check_horizontal(puzzle) + check_vertical(puzzle)
    pprint(diagonals_to_rows(puzzle))

    return xmas_count


def main():
    input_file = "./input.txt"
    print("\n### part 1 ###")
    print(part1(input_file))
    # print("\n### part 2 ###")
    # print(part2(input_file))


if __name__ == "__main__":
    main()
