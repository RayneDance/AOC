import re
f = open("input.txt", "r").readlines()
f = "".join(f)

print(sum([int(x) * int(y) for x, y in re.findall(r"mul\((\d{1,3}),(\d{1,3})\)", re.sub(r"don't\(.*?do\(\)", '', f))]))