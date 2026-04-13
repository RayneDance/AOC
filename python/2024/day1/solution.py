
l1 = []
l2 = []

with open("input.txt", "r") as f:
    for line in f:
        parts = line.split("   ")
        l1.append(int(parts[0]))
        l2.append(int(parts[1]))

l1.sort()
l2.sort()
result = 0

appearances = {}

for i in range(len(l1)):
    result += abs(l1[i] - l2[i])
    if l1[i] not in appearances.keys():
        appearances[l1[i]] = 0

for i in appearances.keys():
    appearances[i] = l2.count(i)

similarities = 0
for i, j in appearances.items():
    similarities += i * j

print(result)
print(similarities)