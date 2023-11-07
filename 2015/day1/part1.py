from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text()
# print(data)

floor = 0

for brackets in data:
    if brackets == "(":
        floor += 1
    elif brackets == ")":
        floor -= 1

print(floor)