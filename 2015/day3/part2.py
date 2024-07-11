from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip()

# print(data)
visited = set()
santa_directions = []
robo_directions = []
santa_coordinate = (0, 0)
robo_coordinate = (0, 0)

for direction in range(0, len(data)):
    if direction % 2:
        robo_directions.append(data[direction])
    else:
        santa_directions.append(data[direction])

for santa_direction in santa_directions:
    visited.add(santa_coordinate)
    if santa_direction == "^":
        santa_coordinate = (santa_coordinate[0], santa_coordinate[1] + 1)
    elif santa_direction == "v":
        santa_coordinate = (santa_coordinate[0], santa_coordinate[1] - 1)
    elif santa_direction == ">":
        santa_coordinate = (santa_coordinate[0] + 1, santa_coordinate[1])
    else:
        santa_coordinate = (santa_coordinate[0] - 1, santa_coordinate[1])

for robo_direction in robo_directions:
    visited.add(robo_coordinate)
    if robo_direction == "^":
        robo_coordinate = (robo_coordinate[0], robo_coordinate[1] + 1)
    elif robo_direction == "v":
        robo_coordinate = (robo_coordinate[0], robo_coordinate[1] - 1)
    elif robo_direction == ">":
        robo_coordinate = (robo_coordinate[0] + 1, robo_coordinate[1])
    else:
        robo_coordinate = (robo_coordinate[0] - 1, robo_coordinate[1])

print("Answer to part 2 : ", len(visited))