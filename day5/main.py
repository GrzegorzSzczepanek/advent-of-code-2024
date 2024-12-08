from os import times_result
from typing import Union, Tuple


def read_file(filepath: str) -> str:
    return open(filepath, "r").read().strip()


def prepare_rules(rules: str) -> list:
    new_ruleset: list[tuple[str, str]] = []
    for rule in rules.strip().split("\n"):
        new_ruleset.append((rule.split("|")[0], rule.split("|")[1]))

    return new_ruleset


def create_rules_dict(rules: list[tuple[str, str]]):
    ruleset = {}

    all_numbers = set(left for left, _ in rules) | set(right for _, right in rules)
    for num in all_numbers:
        ruleset[num] = []

    for left, right in rules:
        if left not in ruleset[right]:
            ruleset[right].append(left)

    return ruleset


def is_valid_2(row: list[str], ruleset: dict) -> Union[Tuple[str, str], bool]:
    page_indices = {page: idx for idx, page in enumerate(row)}

    for right_page, left_pages in ruleset.items():
        if right_page in page_indices:
            for left_page in left_pages:
                if left_page in page_indices:
                    if page_indices[left_page] > page_indices[right_page]:
                        print(left_page, right_page)
                        return left_page, right_page

    return True


def is_valid_update(row: list[str], ruleset: dict) -> bool:

    page_indices = {page: idx for idx, page in enumerate(row)}

    for right_page, left_pages in ruleset.items():
        if right_page in page_indices:
            for left_page in left_pages:
                if left_page in page_indices:
                    if page_indices[left_page] > page_indices[right_page]:
                        print(
                            "false: ",
                            page_indices[left_page],
                            left_page,
                            page_indices[right_page],
                            right_page,
                        )
                        return False

    return True


def part2(input_file: str) -> int:
    result = 0
    content = read_file(input_file)
    try:
        rules_section, pages_section = content.split("\n\n")
    except ValueError:
        print(
            "Input file is not properly formatted. Ensure there's a double newline separating rules and updates."
        )
        return 0

    rules = prepare_rules(rules_section)
    pages_rows = [x.strip().split(",") for x in pages_section.strip().split("\n")]
    ruleset = create_rules_dict(rules)

    for i in range(len(pages_rows)):
        was_corrected = False
        max_iterations = 1000  # infinite loop prevention lmao
        iterations = 0

        while True:
            validation = is_valid_2(pages_rows[i], ruleset)

            if validation == True:
                if was_corrected:
                    middle_index = len(pages_rows[i]) // 2
                    middle_page = pages_rows[i][middle_index]
                    result += int(middle_page)
                break

            if isinstance(validation, tuple):
                left_page, right_page = validation
                left_idx = pages_rows[i].index(left_page)
                right_idx = pages_rows[i].index(right_page)
                pages_rows[i][left_idx], pages_rows[i][right_idx] = (
                    pages_rows[i][right_idx],
                    pages_rows[i][left_idx],
                )
                was_corrected = True

            iterations += 1
            if iterations > max_iterations:
                print("Error: Infinite loop detected in corrections.")
                return 0

    return result


def part1(input_file: str) -> int:
    result = 0
    content = read_file(input_file)
    try:
        rules_section, pages_section = content.split("\n\n")
    except ValueError:
        print(
            "Input file is not properly formatted. Ensure there's a double newline separating rules and updates."
        )
        return 0

    rules = prepare_rules(rules_section)
    pages_rows = [x.strip().split(",") for x in pages_section.strip().split("\n")]
    ruleset = create_rules_dict(rules)

    for row in pages_rows:
        if is_valid_update(row, ruleset):
            middle_index = len(row) // 2
            middle_page = int(row[middle_index])
            result += middle_page
        # else:
        #     print(f"Invalid update: {row}")

    # print("\nRuleset:")
    # for key, values in ruleset.items():
    #     print(f"{key}: {values}")

    return result


def main():
    input_file = "./input.txt"
    print("\n### part 1 ###")
    print(part1(input_file))

    print("\n### part 2 ###")
    print(part2(input_file))


if __name__ == "__main__":
    main()
