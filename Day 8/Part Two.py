def get_num_visible(me: int, trees_closest_first: list) -> int:
    """ Returns the number of elements in the array from the beginning
    through the first element greater than or equal to 'me' """
    if not trees_closest_first:
        return 0
    count = 0
    for elem in trees_closest_first:
        count += 1
        if elem >= me:
            break
    return count

largest_visibility_score = 0
with open("Day 8\input.txt", "r") as f:
    input_arr = [[int(x) for x in line] for line in f.read().splitlines()]
for i, row in enumerate(input_arr):
    for j, value in enumerate(row):
        if i == 50 and j == 50:
            i = 50
        above = [input_arr[k][j] for k in range(0,i)]
        above.reverse()
        visible_above = get_num_visible(value, above)

        below = [input_arr[k][j] for k in range(i+1,len(row))]
        visible_below = get_num_visible(value, below)

        left = input_arr[i][:j]
        left.reverse()
        visible_left = get_num_visible(value, left)

        right = input_arr[i][j+1:]
        visible_right = get_num_visible(value, right)

        visibility_score = visible_above * visible_below * visible_left * visible_right

        if visibility_score > largest_visibility_score:
            largest_visibility_score = visibility_score

print(largest_visibility_score)