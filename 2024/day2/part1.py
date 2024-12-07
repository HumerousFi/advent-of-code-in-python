from pathlib import Path
base_path = Path(__file__).parent
reports = base_path.joinpath("input.in").read_text().strip().split("\n")

# print(reports)

answer = 0

def is_safe(level):
    inc = level[1] > level[0]
    if inc:
        for i in range(1,len(level)):
            diff = level[i] - level[i-1]
            if not 1 <= diff <= 3:
                return False
        return True
    else:
        for i in range(1,len(level)):
            diff = level[i] - level[i-1]
            if not -3 <= diff <= -1:
                return False
        return True

for levels in reports:
    level = [int(i) for i in levels.split()]
    answer += is_safe(level)

print("Answer to part 1 :",answer)