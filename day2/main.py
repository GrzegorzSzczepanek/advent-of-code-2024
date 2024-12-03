def read_file_content(path: str) -> str:
    file = open(path, "r").read()
    return file


def part1(path: str) -> int:
    content = read_file_content(path).strip().split("\n")
    safe_reports = 0

    for line in content:
        levels = list(map(int, line.strip().split()))
        diffs = [levels[i] - levels[i - 1] for i in range(1, len(levels))]

        increasing = all(d > 0 for d in diffs)
        decreasing = all(d < 0 for d in diffs)

        if not (increasing or decreasing):
            continue

        if all(1 <= abs(d) <= 3 for d in diffs):
            safe_reports += 1

    return safe_reports


if __name__ == "__main__":
    print(part1("./input.txt"))
