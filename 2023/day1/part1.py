from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split()

# print(data)

answer = 0

for lines in data:
    digits = [char for char in lines if char.isdigit()]
    calibration = int(digits[0] + digits[-1])
    answer += calibration

print("Answer to part 1 : ", answer)