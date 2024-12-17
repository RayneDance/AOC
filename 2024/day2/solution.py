puzzle = []

with open("input.txt", "r") as f:
    for line in f:
        puzzle.append([int(x) for x in line.split(" ")])

def increasing_check(x):
    for i in range(len(x)-1):
        if x[i] >= x[i+1]:
            return False
        if x[i+1] - x[i] > 3:
            return False
    return True

def decreasing_check(x):
    for i in range(len(x)-1):
        if x[i] <= x[i+1]:
            return False
        if x[i] - x[i+1] > 3:
            return False
    return True

def produce_permutations(s):
    permsx = []
    for i in range(len(s)):
        x = s.copy()
        x.pop(i)
        perms.append(x)
    return permsx

p1 = 0
p2 = 0
for line in puzzle:
    safety = decreasing_check(line) or increasing_check(line)
    p1 += 1 * safety

    if not safety:
        perms = produce_permutations(line)
        for perm in perms:
            safety |= decreasing_check(perm) or increasing_check(perm)

    p2 += 1 * safety

print(f"Part 1: {p1}")
print(f"Part 2: {p2}")


