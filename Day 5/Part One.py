class Stacks():
    def __init__(self, input: str):
        self.stack_commands = ""
        self.stack_array = []
        self.parse_diagram(input)

        for line in self.stack_commands.splitlines():
            self.move_one(*parse_one(line))
        
        for stack_ in self.stack_array:
            print(stack_.pop(), end="")
    
    def parse_diagram(self, input: str):
        pass
        # A blank line separates the diagram from the commands, so can use .split("\n\n") to divide
        # input into diagram and commands.
        input_arr = input.split("\n\n")
        stack_map = input_arr[0]
        self.stack_commands = input_arr[1]
        # Then I think if I strip out [] and spaces I can use a 2D array temporarily...
        # Need one of the four spaces as a placeholder though.
        stack_map = stack_map.replace("] [", "")        
        stack_map = stack_map.replace("]", "")
        stack_map = stack_map.replace("[", "")
        stack_map = stack_map.replace("        ", "--")
        stack_map = stack_map.replace("     ", "-")
        stack_map = stack_map.replace("    ", "-")
        stack_map = stack_map.replace(" ", "")
        stack_map = stack_map.replace("   ", "")
        stack_arr = [[x for x in line] for line in stack_map.splitlines()]
        stack_arr = [list(x) for x in zip(*stack_arr)]
        for i, line in enumerate(stack_arr):
            self.stack_array.append(line.copy())
            for j, x in enumerate(line):
                self.stack_array[i][len(line)-j-1] = x
                if x == '-' or j == len(line)-1:
                    del self.stack_array[i][len(line)-j-1]

    def move_one(self, num_to_move, source_index, destination_index):
        for unused in range(num_to_move):
            self.stack_array[destination_index].append(self.stack_array[source_index].pop())


def parse_one(line: str) -> tuple:
    """ Returns (num_to_move, source_index, destination_index)
    """
    line_arr = line.split()
    return int(line_arr[1]), int(line_arr[3]) - 1, int(line_arr[5]) - 1

with open("input.txt", "r") as f:
    input = f.read()
Stacks(input)