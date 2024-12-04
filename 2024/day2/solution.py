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

def d_increasing_check(x):
    for i in range(len(x)-1):
        if x[i] >= x[i+1] or x[i+1] - x[i] > 3:
            y = x.copy()
            z = x.copy()
            y.pop(i)
            z.pop(i+1)
            return decreasing_check(y) or decreasing_check(z)
    return True

def d_decreasing_check(x, forgiveness = True):
    for i in range(len(x)-1):
        if x[i] <= x[i+1] or x[i+1] - x[i] > 3:
            y = x.copy()
            z = x.copy()
            y.pop(i)
            z.pop(i+1)
            return increasing_check(y) or increasing_check(z)
    return True

safe = 0
for line in puzzle:
    safety = False
    if line[0] > line[1]:
        #safety = decreasing_check(line)
        safety = d_decreasing_check(line)
    if line[0] < line[1]:
        #safety = increasing_check(line)
        safety = d_increasing_check(line)
    if line[0] == line[1]:
        if line[1] > line[2]:
            safety = decreasing_check(line[1:])
        if line[1] < line[2]:
            safety = increasing_check(line[1:])
    safe += 1 * safety

print(safe)


