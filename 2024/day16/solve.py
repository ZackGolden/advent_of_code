import heapq
from dataclasses import dataclass, field
from math import inf
from typing import Dict, List, Set, Tuple

UP = (0, -1)
RIGHT = (1, 0)
DOWN = (0, 1)
LEFT = (-1, 0)

DIRS: Set[Tuple[int, int]] = {UP, RIGHT, DOWN, LEFT}


@dataclass(order=True)
class Vertex:
    x: int = field(compare=False)
    y: int = field(compare=False)
    explored: bool = field(compare=False, default=False)
    distance: float = inf
    previous: Tuple[int, int] = field(compare=False, default=(0, 0))


def walk(
    current: Tuple[int, int], dir: Tuple[int, int], distance: int, maze: List[str]
):
    while True:
        if maze[current[1]][current[0]] == "E":
            return (current, distance)
        paths = 0
        for d in DIRS:
            if maze[current[1] + d[1]][current[0] + d[0]] in {
                ".",
                "E",
                "S",
            }:
                paths += 1
        if paths == 1:  # Dead End
            return (current, distance)
        if paths > 2:  # At a node
            return (current, distance)
        if paths == 2:  # Continue or bend
            if maze[current[1] + dir[1]][current[0] + dir[0]] not in {
                ".",
                "E",
            }:
                return (current, distance)
            else:
                current=(current[0] + dir[0], current[1] + dir[1])
                distance+= 1


def explore(start: Vertex, end: Vertex, maze: List[str]):
    graph: Dict[Tuple[int, int], Vertex] = dict()
    graph[(start.x, start.y)] = start
    graph[(end.x, end.y)] = end
    queue = []
    heapq.heappush(queue, start)
    heapq.heappush(queue, end)

    while True:
        current = heapq.heappop(queue)
        while current.explored:
            current = heapq.heappop(queue)
        if end.distance <= current.distance:
            return end
        for d in DIRS:
            # Don't go Backwards
            if current.previous == d:
                continue
            if maze[current.y + d[1]][current.x + d[0]] in {
                ".",
                "E",
                "S",
            }:
                additional_distance = 0
                if current.previous not in {(0,0), (d[0]* -1, d[1]* -1)}:
                    additional_distance += 1000
                ((x, y), distance) = walk(
                    current=(current.x + d[0], current.y + d[1]),
                    dir=d,
                    distance=current.distance + 1 + additional_distance,
                    maze=maze,
                )
                if (x, y) in graph:
                    v = graph[(x, y)]
                    if v.explored:
                        continue
                    if distance < v.distance:
                        v.distance = distance
                        v.previous = (d[0] * -1, d[1] * -1)
                        if v is not end:
                            heapq.heappush(queue, v)
                else:
                    v = Vertex(x, y, False, distance, (d[0] * -1, d[1] * -1)
)
                    heapq.heappush(queue, v)
        current.explored = True
        graph[(current.x,current.y)] = current


def part_1(lines) -> float:
    start: Vertex | None = None
    end: Vertex | None = None

    # Search for the beginning and the end
    for y, line in enumerate(lines):
        current = []
        for x, c in enumerate(line):
            if c == "S":
                start = Vertex(x=x, y=y, distance=0)
            elif c == "E":
                end = Vertex(x=x, y=y)
            current.append(c)

    if end is None or start is None:
        return inf

    explore(start=start, end=end, maze=lines)

    return end.distance + 1000


def part_2(lines):
    sum = 0
    return sum


def main():
    f = open("./day16/input", "r")
    lines = f.readlines()
    print("Day 16")
    print("Part 1:", part_1(lines))
    print("Part 2:", part_2(lines))


if __name__ == "__main__":
    main()
