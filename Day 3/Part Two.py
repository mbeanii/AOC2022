def calculate_priority(_str: str) -> int:
    """ Computes a priority value given a single character string

    Inputs:
        _str (str) : A single character string
    
    Outputs:
        A priority value as defined by AOC

    Raises:
        Nothing
    """
    upper_character = _str[0].upper()
    return ord(upper_character) - ord('A') + 1 + (26 if upper_character == _str[0] else 0)


if __name__ == "__main__":
    with open("inputs.txt", "r") as f:
        input_list = f.read().splitlines()

    sum = 0
    i = 2
    while i < len(input_list):
        first  = set(input_list[i])
        second = set(input_list[i-1])
        third = set(input_list[i-2])
        
        intersection = first & second & third

        sum += calculate_priority(intersection.pop())
        i += 3

    print(sum)
