from __future__ import annotations
import re
import math

NODE_PATTERN = r"([A-Z\d]+) = \(([A-Z\d]+), ([A-Z\d]+)\)"


class Node:
    def __init__(self, id_: str, left: Node, right: Node) -> None:
        self.id = id_
        self.left = left
        self.right = right

    @classmethod
    def from_line(cls, line: str) -> Node:
        matches = re.match(NODE_PATTERN, line)
        id_, left, right = matches.groups(0)
        return Node(id_, left, right)


def main() -> None:
    lines = read_lines("input.txt")

    instructions = lines.pop(0)
    lines.pop(0)  # skip line

    nodes = {}
    starting_nodes = []
    for line in lines:
        node = Node.from_line(line)
        nodes[node.id] = node
        if node.id.endswith("A"):
            starting_nodes.append(node)

    def get_n_traversals(node: Node) -> int:
        current_node = node
        n_traversals = 0
        while not current_node.id.endswith("Z"):
            for instruction in instructions:
                if instruction == "R":
                    current_node = nodes[current_node.right]
                else:
                    current_node = nodes[current_node.left]
                n_traversals += 1
        return n_traversals

    total_n_traverslals = []
    for node in starting_nodes:
        n = get_n_traversals(node)
        total_n_traverslals.append(n)

    print(math.lcm(*total_n_traverslals))


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
