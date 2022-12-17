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

for line in input_arr:
    line = line.strip()
    command = line.split(" ")
    
    num_cycles = set_num_cycles(command[0])

    for i in range(num_cycles):
        crt_pos = cycle_counter % 40
        cycle_counter += 1
        
        if crt_pos in (register-1, register, register+1):
            print("#", end="")
        else:
            print(".", end="")
        if crt_pos == 39:
            print()
        
        if i == 1:
            value = int(command[1])
            register += value