from collections import defaultdict, deque


class OrderingGraph:
    def __init__(self):
        # Maps each number to a set of numbers that must come after it
        self.adjacency_list = defaultdict(set)
        # Set of all unique numbers in the graph
        self.all_nodes = set()

    def add_ordering_rule(self, preceding_number, succeeding_number):
        """
        Adds a rule that 'preceding_number' must come before 'succeeding_number'.
        """
        self.adjacency_list[preceding_number].add(succeeding_number)
        self.all_nodes.update([preceding_number, succeeding_number])

    def initialize_graph(self, ordering_rules):
        """
        Initializes the graph with a list of ordering rules.
        Each rule is a tuple (preceding_number, succeeding_number).
        """
        for preceding_number, succeeding_number in ordering_rules:
            self.add_ordering_rule(preceding_number, succeeding_number)

    def perform_topological_sort(self):
        """
        Performs topological sorting on the graph.
        Returns a list of numbers in a valid order or raises an exception if a cycle is detected.
        """
        # Initialize in-degree of each node to zero
        in_degree_counts = {node: 0 for node in self.all_nodes}

        for preceding_number in self.adjacency_list:
            for succeeding_number in self.adjacency_list[preceding_number]:
                in_degree_counts[succeeding_number] += 1

        # Initialize a queue with nodes that have in-degree of zero (no dependencies)
        nodes_with_no_dependencies = deque(
            [node for node in self.all_nodes if in_degree_counts[node] == 0]
        )
        sorted_order = []

        while nodes_with_no_dependencies:
            current_number = nodes_with_no_dependencies.popleft()
            sorted_order.append(current_number)

            for succeeding_number in self.adjacency_list[current_number]:
                in_degree_counts[succeeding_number] -= 1
                if in_degree_counts[succeeding_number] == 0:
                    nodes_with_no_dependencies.append(succeeding_number)

        if len(sorted_order) != len(self.all_nodes):
            raise Exception("Cycle detected! No valid ordering possible")

        return sorted_order

    def is_preceding_number_before(self, preceding_number, succeeding_number):
        """
        Checks if 'preceding_number' must come before 'succeeding_number' based on the rules.
        Returns True if there is a path from 'preceding_number' to 'succeeding_number', else False.
        """
        visited_numbers = set()
        numbers_to_visit = [preceding_number]

        while numbers_to_visit:
            current_number = numbers_to_visit.pop()
            if current_number == succeeding_number:
                return True
            if current_number not in visited_numbers:
                visited_numbers.add(current_number)
                numbers_to_visit.extend(self.adjacency_list[current_number])

        return False


def read_file(filepath: str) -> str:
    return open(filepath, "r").read().strip()


def prepare_rules(rules: str) -> list:
    ruleset = rules.strip().split("\n")
    new_ruleset: list[tuple[str, str]] = []
    for rule in rules.strip().split("\n"):
        new_ruleset.append((rule.split("|")[0], rule.split("|")[1]))

    print(new_ruleset)
    return new_ruleset


def part1(input_file: str) -> int:
    result = 0
    content = read_file(input_file)
    rules, pages_rows = content.split("\n\n")

    # for page_row in pages_rows.strip().split("\n"):
    #     curr_pages_row = page_row.split(",")
    #     for page in curr_pages_row:
    #         ...

    rules = prepare_rules(rules)
    ordering_graph = OrderingGraph()
    ordering_graph.initialize_graph(rules)

    try:
        valid_ordering = ordering_graph.perform_topological_sort()
        print("Valid Ordering:", valid_ordering)
    except Exception as error:
        print(str(error))

    print(
        "Should 47 come before 53?",
        ordering_graph.is_preceding_number_before("47", "53"),
    )
    print(
        "Should 53 come before 47?",
        ordering_graph.is_preceding_number_before("53", "47"),
    )

    return result


def main():
    input_file = "./input.txt"
    print("\n### part 1 ###")
    print(part1(input_file))


if __name__ == "__main__":
    main()
