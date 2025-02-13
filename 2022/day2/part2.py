from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath('input.in').read_text().strip().split('\n')

# print(data)

count = 0
answer = 0

for pair in data:
    if pair[0] == "A" and pair[2] == "X":
        count += 3
    elif pair[0] == "B" and pair[2] == "Y":
        count += 5
    elif pair[0] == "C" and pair[2] == "Z":
        count += 7
    elif pair[0] == "A" and pair[2] == "Z":
        count += 8
    elif pair[0] == "B" and pair[2] == "X":
        count += 1
    elif pair[0] == "C" and pair[2] == "Y":
        count += 6
    elif pair[0] == "C" and pair[2] == "X":
        count += 2
    elif pair[0] == "A" and pair[2] == "Y":
        count += 4
    elif pair[0] == "B" and pair[2] == "Z":
        count += 9
    answer += count
    count = 0

print(answer)