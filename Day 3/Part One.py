def create_map(_str: str) -> dict:
    """ Creates a dict which maps letters in the provided string to point values

    Inputs:
        _str (str) : A string composed of capital and lowercase letters
    
    Outputs:
        A dictionary with characters from _str as keys and point values.

    Raises:
        Nothing
    """
    _map = {}

    for character in _str:
        upper_character = character.upper()
        _map[character] = ord(upper_character) - ord('A') + 1 + (26 if upper_character == character else 0)
    
    return _map



with open("input.txt", "r") as f:
    input_list = f.read().splitlines()

sum = 0
for line in input_list:
    half_mark = int(len(line)/2)

    left  = line[:half_mark]
    right = line[half_mark:]

    _map = create_map(right)

    for character in left:
        if character in _map:
            sum += _map[character]
            break

print(sum)
