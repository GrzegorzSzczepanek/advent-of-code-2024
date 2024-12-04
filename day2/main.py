def read_file_content(path: str) -> str:
    file = open(path, "r").read()
    return file


def is_safe(levels: list[int]) -> bool:
    diffs = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

    increasing = all(d > 0 for d in diffs)
    decreasing = all(d < 0 for d in diffs)

    if not (increasing or decreasing):
        return False

    if all(1 <= abs(d) <= 3 for d in diffs):
        return True

    return False


def part1(path: str) -> int:
    content = read_file_content(path).strip().split("\n")
    safe_reports = 0

    for line in content:
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            safe_reports += 1

    return safe_reports


def part2(path: str) -> int:

    content = read_file_content(path).strip().split("\n")
    safe_reports = 0

    for line in content:
        levels = list(map(int, line.strip().split()))
        if is_safe(levels):
            safe_reports += 1
        else:
            for i in range(len(levels)):
                if is_safe(levels[:i] + levels[i + 1 :]):
                    safe_reports += 1
                    break

    return safe_reports


if __name__ == "__main__":
    print("### part 1 ###")
    print(part1("./input.txt"))

    print("### part 1 ###")
    print(part2("./input.txt"))
