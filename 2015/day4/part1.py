from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text()

# print(data)

import hashlib

incrementable_character = 1

while True:
    text = data + str(incrementable_character)
    result = hashlib.md5(text.encode())
    # print(result.hexdigest())
    if result.hexdigest().startswith("00000"):
        break
    incrementable_character += 1

print("Answer to part 1 : ", incrementable_character)