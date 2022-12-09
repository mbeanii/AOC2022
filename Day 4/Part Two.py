with open("input.txt", "r") as f:
    input_list = f.read().splitlines()

count = 0
for line in input_list:
    outer = [inner.split("-") for inner in line.split(",")]
    set1 = set(range(int(outer[0][0]), int(outer[0][1])+1))
    set2 = set(range(int(outer[1][0]), int(outer[1][1])+1))
    intersection = set1 & set2
    if(len(intersection)):
        count += 1
print(count)
