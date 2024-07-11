from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split("\n")

count = 0
highest = 0
cal = []

for cals in data:
    if cals == '':
        count = 0
    else:
        cals = int(cals)
        count += cals
        cal.append(count)
    if count > highest:
        highest = count
cal.sort()
print("answer to part 2 : " , sum(cal[-3:]))