with open("input.txt", "r") as f:
    input = f.read()

i = 14
while i < len(input):
    window = input[i-14:i]
    if len(window) == len(set(window)):
        print(i)
        break
    i += 1
