import itertools

class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.puzzle = {int(line.split(":")[0]): [int(x) for x in line.split(":")[1].strip().split(" ")] for line in self.file_text}


def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def conc(a, b):
    return int(str(a) + str(b))

def extended_permutations(iterable, r):
    return itertools.product(iterable, repeat=r)

def search(puzzle, ops):
    k = puzzle[0]
    v = puzzle[1]
    p_sz = len(v) - 1
    perms = extended_permutations(ops, p_sz)

    for perm in perms:
        res = v[0]
        for i, p in enumerate(perm):
            res = p(res, v[i+1])
        if res == k:
            return k
    return 0


def main():
    s = Solution()
    part1 = 0
    part2 = 0
    for item in s.puzzle.items():
        #print(item, search(item))
        part1 += search(item, [add, mul])
        part2 += search(item, [add, mul, conc])

    print(part1)
    print(part2)



if __name__ == "__main__":
    main()