from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split()

# print(data)

nice = []
naughty = []

for string in data:
    if sum(char in "aeiou" for char in string) >= 3 and any(string[index] == string[index + 1] for index in range(len(string) - 1)) and not any(term in string for term in ["ab", "cd", "pq", "xy"]):
        nice.append(string)
    else:
        naughty.append(string)

print("Answer to part 1 : ", len(nice))