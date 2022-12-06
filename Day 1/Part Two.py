with open("input.txt", "r") as f:
    input = f.read()

rations = input.split("\n\n")

rations_nested_list = [x.split("\n") for x in rations]

rations_nested_list_of_int = [[int(x) for x in lst] for lst in rations_nested_list]

list_of_sums = [sum(lst) for lst in rations_nested_list_of_int]

list_of_sums.sort()

print(sum(list_of_sums[-3:]))
