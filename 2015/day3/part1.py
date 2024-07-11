from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip()

# print(data)

visited = set()
visited.add((0, 0))
position = (0, 0)

for direction in data:
    if direction == "^":
        position = (position[0], position[1] + 1)
    elif direction == "v":
        position = (position[0], position[1] - 1)
    elif direction == ">":
        position = (position[0] + 1, position[1])
    else:
        position = (position[0] - 1, position[1])
    visited.add(position)

print("Answer to part 1 : ", len(visited))