from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split()

# print(data)

l1 = []
l2 = []

for nums in enumerate(data):
    # print(nums)
    if nums[0] % 2 == 0:
        l1.append(int(nums[1]))
    else:
        l2.append(int(nums[1]))
    
freq = 0
answer = 0

for n in l1:
    for x in l2:
        if n == x:
            freq += 1
    answer += n * freq
    freq = 0

print("Answer to part 2 :",answer)