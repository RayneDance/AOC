class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.puzzle = [line.strip() for line in self.file_text]
        self.nodes = []
        self.node_dict = {}
        for row in self.puzzle:
            self.nodes.append([])
            for column in row:
                self.nodes[-1].append(Node(column, (self.puzzle.index(row), row.index(column))))
                if self.nodes[-1][-1].val != ".":
                    if self.nodes[-1][-1].val in self.node_dict:
                        self.node_dict[self.nodes[-1][-1].val].append(self.nodes[-1][-1])
                    else:
                        self.node_dict[self.nodes[-1][-1].val] = [self.nodes[-1][-1]]
        self.sz_h = len(self.puzzle[0])
        self.sz_w = len(self.puzzle)


class Node:
    def __init__(self, val, pos):
        self.val = val
        self.pos = pos
        self.antinodes = False

def get_slope(a, b):
    return (b[0] - a[0], b[1] - a[1])

def get_lcd_slope(slope, a, b):
    # Find a divisor of a and b if exists
    for i in range(1, min(slope[0], slope[1])+1):
        if slope[0] % i == 0 and slope[1] % i == 0:
            return (int(slope[0]/i), int(slope[1]/i))
    return slope

def plot_antinodes(slope, a, b, s):
    antinode1 = (b[0] + slope[0], b[1] + slope[1])
    slope = invert_slope(slope)
    antinode2 = (a[0] + slope[0], a[1] + slope[1])

    # Check bounds of puzzle:
    if check_bounds(antinode1, s):
        s.nodes[antinode1[0]][antinode1[1]].antinodes = True
    if check_bounds(antinode2, s):
        s.nodes[antinode2[0]][antinode2[1]].antinodes = True

def plot_antinodes_all(slope, a, b, s):
    slope = get_lcd_slope(slope, a, b)
    antinode1 = (b[0] + slope[0], b[1] + slope[1])
    s.nodes[a[0]][a[1]].antinodes = True
    s.nodes[b[0]][b[1]].antinodes = True
    while check_bounds(antinode1, s):
        s.nodes[antinode1[0]][antinode1[1]].antinodes = True
        antinode1 = (antinode1[0] + slope[0], antinode1[1] + slope[1])

    slope = invert_slope(slope)
    antinode1 = (b[0] + slope[0], b[1] + slope[1])
    while check_bounds(antinode1, s):
        s.nodes[antinode1[0]][antinode1[1]].antinodes = True
        antinode1 = (antinode1[0] + slope[0], antinode1[1] + slope[1])

def invert_slope(slope):
    return (-slope[0], -slope[1])

def check_bounds(a, s):
    if (0 <= a[0] < s.sz_w and 0 <= a[1] < s.sz_h):
        return True
    return False

def write_to_file(s):
    text = ""
    for row in s.nodes:
        for node in row:
            if node.antinodes:
                text += "#"
            else:
                text += node.val
        text += "\n"
    open("output.txt", "w").write(text)


def main():
    s = Solution()
    antinodes = 0
    for k, v in s.node_dict.items():
        for i in range(len(v)):
            for j in range(i+1, len(v)):
                slope = get_slope(v[i].pos, v[j].pos)
                plot_antinodes(slope, v[i].pos, v[j].pos, s)
                plot_antinodes_all(slope, v[i].pos, v[j].pos, s)

    for row in s.nodes:
        for node in row:
            antinodes += 1 * node.antinodes
    #write_to_file(s)
    print(antinodes)

if __name__ == "__main__":
    main()