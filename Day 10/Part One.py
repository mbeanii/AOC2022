INTERESTING_NUMS = [20, 60, 100, 140, 180, 220]

class UnrecognizedCommandError(Exception):
    pass


def set_num_cycles(command: list) -> int:
    if command == "noop":
        return 1
    elif command == "addx":
        return 2
    else:
        raise UnrecognizedCommandError(command)


with open("Day 10/input.txt", "r") as f:
    input_arr = f.readlines()

cycle_counter = 0
register = 1
signal_strength_total = 0

for line in input_arr:
    line = line.strip()
    command = line.split(" ")
    
    num_cycles = set_num_cycles(command[0])

    for i in range(num_cycles):
        cycle_counter += 1

        if cycle_counter in INTERESTING_NUMS:
            signal_strength = cycle_counter * register
            signal_strength_total += signal_strength
        
        if i == 1:
            value = int(command[1])
            register += value

print(signal_strength_total)