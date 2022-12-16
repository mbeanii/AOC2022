from copy import copy
from math import floor, ceil

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __eq__(self, other) -> bool:
        return (self.x == other.x and self.y == other.y)

    def __hash__(self) -> int:
        return hash(str(f"{self.x};{self.y}"))
    
    def __repr__(self) -> str:
        return(f"({self.x},{self.y})")


class Model:
    def __init__(self, input):
        self.head = Point()
        self.tail = Point()
        self.visited_set = set()
        for line in input.splitlines():
            line.strip()
            times = int(line[2:])
            for unused in range(times):
                self.move_one(*get_command_deltas(line))
        return
    
    def move_one(self, dx: int, dy: int) -> None:
        self.move_head_one(dx, dy)
        self.move_tail_one(*self.get_tail_deltas())
        return

    def move_head_one(self, dx: int, dy: int) -> None:
        self.head.x += dx
        self.head.y += dy

    def get_tail_deltas(self) -> tuple:
        """ Returns (dx: int, dy: int) tail_deltas, each between
        -1 and 1, to be consumed by move_tail_one."""
        # If the head is ever two steps directly up, down, left, or right from the tail,
        # the tail must also move one step in that direction so it remains close enough
        distance_right = self.head.x - self.tail.x
        distance_above = self.head.y - self.tail.y

        dx = 0
        dy = 0
        ropes_not_touching = (max(abs(distance_right), abs(distance_above)) == 2)

        if ropes_not_touching:
            dx  = floor((distance_right / 2) + 0.5) if distance_right  >= 0.0 else ceil((distance_right / 2)  - 0.5)
            dy  = floor((distance_above / 2) + 0.5) if distance_above  >= 0.0 else ceil((distance_above / 2)  - 0.5)
        
        return(dx, dy)

    def move_tail_one(self, dx: int, dy: int) -> None:
        self.tail.x += dx
        self.tail.y += dy
        self.visited_set.add(copy(self.tail))


def get_command_deltas(line) -> tuple:
    """ Consumes a line of input and returns (dx: int, dy: int)
    to be consumed by move_one"""
    command = line.split(" ")
    if command[0] == "U":
        return (0, 1)
    elif command[0] == "D":
        return (0, -1)
    elif command[0] == "L":
        return (-1, 0)
    elif command[0] == "R":
        return (1, 0)
    else:
        raise ValueError(f"Invalid line {line}")

with open("Day 9\\input.txt", "r") as f:
    input = f.read()
model = Model(input)
print(len(model.visited_set))