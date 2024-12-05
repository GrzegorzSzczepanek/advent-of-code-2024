import re
from math import prod as mProd


def read_file(filepath: str) -> str:
    return open(filepath, "r").read().strip()


def calculate_prod(instruction):
    return mProd(list(map(int, instruction[4:-1].split(","))))


def part1(input_file: str) -> int:
    sum: int = 0
    memory = read_file(input_file)
    instructions = re.findall(r"mul\(\d{1,3},\d{1,3}\)", memory)

    for instruction in instructions:
        sum += mProd(list(map(int, instruction[4:-1].split(","))))

    return sum


def part2(input_file: str) -> int:
    sum = 0

    memory = read_file(input_file)
    patterns = [r"mul\(\d{1,3},\d{1,3}\)", r"do\(\)|don't\(\)"]

    matches = []

    for pattern in patterns:
        for match in re.finditer(pattern, memory):
            matches.append((match.start(), match.group()))

    matches.sort(key=lambda x: x[0])

    ordered_instructions = [match[1] for match in matches]

    enabled = True

    for instruction in ordered_instructions:
        if instruction == "don't()":
            enabled = False
        elif instruction == "do()":
            enabled = True
        else:
            sum += calculate_prod(instruction) if enabled else 0

    return sum


def main():
    input_file = "./input.txt"
    print("\n### part 1 ###")
    print(part1(input_file))
    print("\n### part 2 ###")
    print(part2(input_file))


if __name__ == "__main__":
    main()
