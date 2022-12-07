rps_map = {
    "A": {
        "Z": 0, # Lose
        "Y": 6, # Win
        "X": 4, # Tie
    },
    "B": {
        "X": 0, # Lose
        "Z": 6, # Win
        "Y": 3, # Tie
    },
    "C": {
        "Y": 0, # Lose
        "X": 6, # Win
        "Z": 3, # Tie
    },
    "X": 1,
    "Y": 2,
    "Z": 3,
}

with open("input.txt", "r") as f:
    input_list = f.readlines()

score = 0
for line in input_list:                # Desk check against example
    score += rps_map[line[2]]          # 2 1 3
    score += rps_map[line[0]][line[2]] # 6 0 3

print(score)                           # 8 9 15