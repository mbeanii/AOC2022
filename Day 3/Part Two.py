def calculate_priority(_str: str) -> int:
    """ Computes a priority value given a single character string

    Inputs:
        _str (str) : A single character string
    
    Outputs:
        A priority value as defined by AOC - here a-z are 1-26 with A-Z as 27-52

    Raises:
        Nothing
    """
    upper_character = _str[0].upper()
    return ord(upper_character) - ord('A') + 1 + (26 if upper_character == _str[0] else 0)


with open("input.txt", "r") as f:
    input_list = f.read().splitlines()

sum = 0
i = 2
while i < len(input_list):
    sum += calculate_priority((set(input_list[i]) & set(input_list[i-1])& set(input_list[i-2])).pop())
    i += 3

print(sum)
