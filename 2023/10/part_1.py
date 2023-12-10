from __future__ import annotations
from typing import Optional
from pprint import pprint
from collections import namedtuple
from enum import Enum


Position = namedtuple("Position", ["row", "col"])


class Direction(Enum):
    North = Position(1, 0)
    South = Position(-1, 0)
    East = Position(0, 1)
    West = Position(0, -1)


pipes = {
    "|": (Direction.North, Direction.South),
    "-": (Direction.East, Direction.West),
    "L": (Direction.North, Direction.East),
    "J": (Direction.North, Direction.West),
    "7": (Direction.South, Direction.West),
    "F": (Direction.South, Direction.East),
    ".": (),
}


# class Node:
#     def __init__(
#         self,
#         id_: str,
#         north: Optional[Node] = None,
#         south: Optional[Node] = None,
#         east: Optional[Node] = None,
#         west: Optional[Node] = None,
#     ) -> None:
#         self.id = id_
#         self.north = north
#         self.south = south
#         self.east = east
#         self.west = west


def main() -> None:
    lines = read_lines("sample.txt")

    graph = []

    nodes = {}

    grid = create_2d_list(lines)
    start: Position = None

    for i, row in enumerate(grid):
        for j, col in enumerate(row):
            position = Position(i, j)
            if col == "S":
                start = position
                continue
            id_ = f"{position.row} - {position.col}"
            nodes[id_] = pipes[col]

    # find possible starting directions
    possible_directions = []
    if start.row > 0 and grid[start.row - 1][start.col] in "|7F":
        possible_directions.append(Position(start.row - 1, start.col))
    if start.row < len(grid) and grid[start.row + 1][start.col] in "|LJ":
        possible_directions.append(Position(start.row + 1, start.col))
    if start.col > 0 and grid[start.row][start.col + 1] in "-J7":
        possible_directions.append(Position(start.row, start.col + 1))
    if start.col < len(grid[start.row]) and grid[start.row][start.col - 1] in "-LF":
        possible_directions.append(Position(start.row, start.col - 1))

    print(nodes)
    print(possible_directions)
    # find starting point
    # starting_point: Position | None = None
    # for i, row in enumerate(lines):
    #     if "S" in row:
    #         starting_point = Position(i, row.find("S"))
    #         break

    # if starting_point is None:
    #     raise ValueError("Starting point not found")

    # find possible directions around starting point
    # possible_directions = []
    # if (
    #     starting_point.row > 0
    #     and grid[starting_point.row - 1][starting_point.col] in "|7F"
    # ):
    #     possible_directions.append(Position(starting_point.row - 1, starting_point.col))
    # if (
    #     starting_point.row < len(grid)
    #     and grid[starting_point.row + 1][starting_point.col] in "|LJ"
    # ):
    #     possible_directions.append(Position(starting_point.row + 1, starting_point.col))
    # if (
    #     starting_point.col > 0
    #     and grid[starting_point.row][starting_point.col + 1] in "-J7"
    # ):
    #     possible_directions.append(Position(starting_point.row, starting_point.col + 1))
    # if (
    #     starting_point.col < len(grid[starting_point.row])
    #     and grid[starting_point.row][starting_point.col - 1] in "-LF"
    # ):
    #     possible_directions.append(Position(starting_point.row, starting_point.col - 1))

    # print(f"starting point at {starting_point}")
    # print(f"possible directions {possible_directions}")

    # for direction in possible_directions:
    #     explore_direction(direction, [starting_point])

    # def explore_direction(from_direction: Direction, char: str, seen: list) -> None:
    #     to_direction: Direction | None = None
    #     if char == "|":
    #         if from_direction == Direction.North:
    #             to_direction = Direction.South
    #     if char == "-":
    #         ...
    #     if char == "":
    #         ...
    #     if char == "":
    #         ...
    #     if char == "":
    #         ...
    #     if char == "":
    #         ...
    #     if char == "":
    #         ...
    #     if char == "":
    # ...

    # def get_direction(char: str, position: Position) -> Optional[tuple[Position]]:
    #     north  = south = east = west = None
    #     if col == "|LJ" and position.row > 0:
    #         north = (position.row - 1, position.col)
    #     if col in ""


def create_2d_list(lines: list[str]) -> list[list[str]]:
    return [[char for char in line] for line in lines]


def read_lines(filename: str) -> list[str]:
    with open(filename, "r") as f:
        return f.read().splitlines()


if __name__ == "__main__":
    main()
