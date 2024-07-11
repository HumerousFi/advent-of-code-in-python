from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().splitlines()

# print(data)

wrap_area = 0
ribbon = 0

for values in data:

    lwh = values.split("x")

    length = int(lwh[0])
    width = int(lwh[1])
    height = int(lwh[2])

    ribbon += length * width * height

    if length >= width and length >= height:
        wrap_area += width + width + height + height
    elif width >= length and width >= height:
        wrap_area += length + length + height + height
    else:
        wrap_area += length + length + width + width

print("Answer to part 2 : ", wrap_area + ribbon)