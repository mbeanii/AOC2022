choose_map = {
    "A": {
        "X": 3, # Scissors Lose (3 + 0) = 3
        "Y": 4, # Rock Draw (1 + 3) = 4
        "Z": 8, # Paper Win (2 + 6) = 8
    },
    "B": {
        "X": 1, # Rock Lose (1 + 0) = 1
        "Y": 5, # Paper Draw (2 + 3) = 5
        "Z": 9, # Scissors Win (3 + 6) = 9
    },
    "C": {
        "X": 2, # Paper Lose (2 + 0) = 2
        "Y": 6, # Scissors Draw (3 + 3) = 6
        "Z": 7, # Rock Win (1 + 6) = 7
    }
}

with open("input.txt", "r") as f:
    input_list = f.readlines()

score = 0
for line in input_list:
    score += choose_map[line[0]][line[2]]  # 4 + 1 + 7 = 12

print(score)