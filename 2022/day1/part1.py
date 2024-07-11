from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split("\n")

# print(data)
count = 0
highest = 0

for cals in data:
    if cals == '':
        count = 0
    else:
        cals = int(cals)
        count += cals
    if count > highest:
        highest = count
        
    
print("answer to part 1 : ", highest)