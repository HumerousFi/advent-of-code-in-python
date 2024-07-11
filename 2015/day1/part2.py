from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip()
# print(data)

floor = 0
index = 0
indices = []

for brackets in data:
    if brackets == "(":
        floor += 1
        index += 1
    elif brackets == ")":
        floor -= 1
        index += 1
    if floor == -1:
        indices.append(index)
        
print("Answer to part 2 : ", indices[0])