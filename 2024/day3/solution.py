import re

f = open("input.txt", "r").readlines()
f = "".join(f)
x = r'mul\(\d{1,3},\d{1,3}\)'
regex = re.findall(x, f)

result = 0
result2 = 0
print(len(regex))
for i in regex:
    re2 = re.findall(r'\d+', i)
    result += int(re2[0]) * int(re2[1])
first_section_re = r'^.*?(?=don\'t\(\)|do\(\))'
second_sections_re = r'(?:do\(\)).*?(?:don\'t\(\)|$)'

first = re.match(first_section_re, f)
second = re.findall(second_sections_re, f)

for i in re.findall(x, first.group()):
    re2 = re.findall(r'\d+', i)
    result2 += int(re2[0]) * int(re2[1])

for i in second:
    for j in re.findall(x, i):
        re2 = re.findall(r'\d+', j)
        result2 += int(re2[0]) * int(re2[1])

print(f"Part 1: {result}")
print(f"Part 2: {result2}")