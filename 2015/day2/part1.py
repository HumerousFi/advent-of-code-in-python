from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().splitlines()

# print(data)

surface_area = 0
extra_area = 0

for values in data:

    lwh = values.split("x")

    length = int(lwh[0])
    width = int(lwh[1])
    height = int(lwh[2])

    surface_area += 2 * length * width + 2 * width * height + 2 * height * length
    
    if length >= width and length >= height:
        extra_area += width * height
    elif width >= length and width >= height:
        extra_area += length * height
    else:
        extra_area += length * width

print("Answer to part 1 : ", surface_area + extra_area)