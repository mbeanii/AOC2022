with open("input.txt", "r") as f:
    input = f.read()

i = 4
while i < len(input):
    window = input[i-4:i]
    if len(window) == len(set(window)):
        print(i)
        break
    i += 1
