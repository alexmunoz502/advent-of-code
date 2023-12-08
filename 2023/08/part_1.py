from __future__ import annotations
import re


NODE_PATTERN = r"([A-Z]+) = \(([A-Z]+), ([A-Z]+)\)"


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
    for line in lines:
        node = Node.from_line(line)
        nodes[node.id] = node

    # traversal
    n_traversals = 0
    current_node: Node = nodes["AAA"]

    while current_node.id != "ZZZ":
        for instruction in instructions:
            if instruction == "R":
                current_node = nodes[current_node.right]
            else:
                current_node = nodes[current_node.left]
            n_traversals += 1

    print(n_traversals)


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
