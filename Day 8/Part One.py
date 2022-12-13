with open("Day 8\input.txt", "r") as f:
    input_arr = [[int(x) for x in line] for line in f.read().splitlines()]
print(sum([sum([((max([input_arr[k][j] for k in range(0,i)], default=-1) < value) or (max([input_arr[k][j] for k in range(i+1,len(row))], default=-1) < value) or (max(input_arr[i][:j], default=-1) < value) or (max(input_arr[i][j+1:], default=-1) < value)) for j, value in enumerate(row)]) for i, row in enumerate(input_arr)]))
