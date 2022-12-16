from copy import copy
from math import floor, ceil

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.next = None
    
    def __eq__(self, other) -> bool:
        return (self.x == other.x and self.y == other.y)

    def __hash__(self) -> int:
        return hash(str(f"{self.x};{self.y}"))
    
    def __repr__(self) -> str:
        return(f"({self.x},{self.y})")
    
    def is_tail(self) -> bool:
        return(not bool(self.next))


class Model:
    def __init__(self, input):
        self.head = Point()
        self.init_points(9)
        self.visited_set = set()
        for line in input.splitlines():
            line.strip()
            times = int(line[2:])
            for _ in range(times):
                self.move_one(*get_command_deltas(line))
        return

    def init_points(self, num_points):
        p_point = self.head
        for _ in range(num_points):
          p_point.next = Point()
          p_point = p_point.next
        return
    
    def move_one(self, dx: int, dy: int) -> None:
        self.move_head_one(dx, dy)
        self.move_followers_one(self.head)
        return

    def move_head_one(self, dx: int, dy: int) -> None:
        self.head.x += dx
        self.head.y += dy

    def get_follower_deltas(self, point) -> tuple:
        """ Returns (dx: int, dy: int) tail_deltas, each between
        -1 and 1, to be consumed by move_followers_one.
        
        Inputs:
            point (Point): The leader of the two points to be compared.
                Its point.next will be the follower.
        
        Returns:
            A tuple: (dx, dy) """
        # If the head is ever two steps directly up, down, left, or right from the tail,
        # the tail must also move one step in that direction so it remains close enough
        distance_right = point.x - point.next.x
        distance_above = point.y - point.next.y

        dx = 0
        dy = 0
        ropes_not_touching = (max(abs(distance_right), abs(distance_above)) == 2)

        if ropes_not_touching:
            dx  = floor((distance_right / 2) + 0.5) if distance_right  >= 0.0 else ceil((distance_right / 2)  - 0.5)
            dy  = floor((distance_above / 2) + 0.5) if distance_above  >= 0.0 else ceil((distance_above / 2)  - 0.5)
        
        return(dx, dy)

    def move_followers_one(self, point: Point) -> None:
        """ Recursive method to move each follower, given the head """
        if point.is_tail():
            self.visited_set.add(copy(point))
            return
        
        dx, dy = self.get_follower_deltas(point)
        point.next.x += dx
        point.next.y += dy
        self.move_followers_one(point.next)


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
