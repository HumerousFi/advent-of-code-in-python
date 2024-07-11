from pathlib import Path
base_path = Path(__file__).parent
data = base_path.joinpath("input.in").read_text().strip().split()

# print(data)

digits = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}
