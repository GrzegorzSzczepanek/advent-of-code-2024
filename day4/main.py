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
        row.append("~")
    return row


def diagonals_to_rows(puzzle: list):
    new_lst = []

    for i in range(len(puzzle)):
        diagonal = []
        for j in range(len(puzzle)):
            if i + j < len(puzzle[0]):
                diagonal.append(puzzle[j][i + j])
        new_lst.append(pad_row(diagonal))

    for i in range(1, len(puzzle)):
        diagonal = []
        for j in range(len(puzzle) - i):
            diagonal.append(puzzle[i + j][j])
        new_lst.append(pad_row(diagonal))

    for i in range(len(puzzle[0])):
        diagonal = []
        for j in range(len(puzzle)):
            if i - j >= 0:
                diagonal.append(puzzle[j][i - j])
        new_lst.append(pad_row(diagonal))

    for i in range(1, len(puzzle)):
        diagonal = []
        for j in range(len(puzzle) - i):
            diagonal.append(puzzle[i + j][len(puzzle[0]) - 1 - j])
        new_lst.append(pad_row(diagonal))

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


def check_diagonal(puzzle: list[str]) -> int:
    count = 0

    diagonals = diagonals_to_rows(puzzle)
    diagonals = ["".join(diagonal) for diagonal in diagonals]
    pprint(diagonals)

    count = check_horizontal(diagonals)

    return count


def part2(input_file: str) -> int:
    xmas_count = 0
    puzzle = read_file(input_file).split("\n")

    xmas_layouts = [
        "M.S\n.A.\nM.S",
        "S.M\n.A.\nS.M",
        "S.S\n.A.\nM.M",
        "M.M\n.A.\nS.S",
    ]

    for i in range(1, len(puzzle) - 1):
        for j in range(1, len(puzzle[0]) - 1):
            square = (
                puzzle[i - 1][j - 1]
                + "."
                + puzzle[i - 1][j + 1]
                + "\n"
                + "."
                + puzzle[i][j]
                + "."
                + "\n"
                + puzzle[i + 1][j - 1]
                + "."
                + puzzle[i + 1][j + 1]
            )

            if square in xmas_layouts:
                xmas_count += 1

    return xmas_count


def part1(input_file: str) -> int:
    xmas_count = 0

    puzzle = read_file(input_file).split("\n")
    xmas_count += (
        check_horizontal(puzzle) + check_vertical(puzzle) + check_diagonal(puzzle)
    )
    pprint(diagonals_to_rows(puzzle))

    return xmas_count


def main():
    input_file = "./input.txt"
    # print("\n### part 1 ###")
    # print(part1(input_file))
    print("\n### part 2 ###")
    print(part2(input_file))


if __name__ == "__main__":
    main()
