from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip()
# print(data)

floor = 0

for brackets in data:
    if brackets == "(":
        floor += 1
    elif brackets == ")":
        floor -= 1

print("Answer to part 1 : ", floor)