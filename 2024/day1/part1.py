from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split()

# print(data)

a = []
b = []

for i , n in enumerate(data):
    # print(i,n)
    if i % 2 == 0:
        a.append(int(n))
    else:
        b.append(int(n))

a.sort()
b.sort()

answer = sum(abs(a[n]-b[n]) for n in range(len(a)))

print("Answer to part 1 :",answer)