from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split(", ")

# print(data)

facing = "N"
x, y = 0, 0
left = {"N" : "W" , "W" : "S" , "S" : "E" , "E" : "N"}
right = {"W" : "N" , "S" : "W" , "E" : "S" , "N" : "E"}

for instructions in data:

    magnitude = int(instructions[1:])
    
    if instructions[0] == "L":
        facing = left[facing]
    else:
        facing = right[facing]
    
    if facing == "N":
        y += magnitude
    elif facing == "E":
        x += magnitude
    elif facing == "S":
        y -= magnitude
    else:
        x -= magnitude

print("Answer to part 1 : ", x + y)