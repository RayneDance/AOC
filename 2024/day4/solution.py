

class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        for l in range(len(self.file_text)):
            self.file_text[l] = self.file_text[l].strip()
        self.search_forward = "XMAS"
        self.search_backward = self.search_forward[::-1]

    def check_forward(self, line):
        found = 0
        if line == self.search_forward:
            found += 1
        if line == self.search_backward:
            found += 1
        return found

    def check_diagonal(self, grid):
        found = 0

        for key in [self.search_forward, self.search_backward]:
            grid_found = ''
            for l in range(4):
                if grid[l][l] == key[l]:
                    grid_found += grid[l][l]
            if grid_found == key:
                found += 1

            if grid[0][3] == key[0]:
                if grid[1][2] == key[1]:
                    if grid[2][1] == key[2]:
                        if grid[3][0] == key[3]:
                            found += 1

        return found


    @staticmethod
    def filter_to_mas(grid):
        grid = [list(x) for x in grid]
        #print(grid)

        grid[0][1] = '.'
        grid[1][0] = '.'
        grid[1][2] = '.'
        grid[2][1] = '.'

        for i in range(3):
            grid[i] = ''.join(grid[i])

        return grid




def main(s):
    count = 0
    xcount = 0
    for i in range(len(s.file_text)):
        for j in range(len(s.file_text[i])):
            forward_found = 0
            if j < len(s.file_text[i]) - 3:
                ln = s.file_text[i][j:j+4]
                forward_found = s.check_forward(ln)
            grid_found = 0
            if i < len(s.file_text) - 3:
                dn = s.file_text[i][j] + s.file_text[i + 1][j] + s.file_text[i + 2][j] + s.file_text[i + 3][j]
                count += s.check_forward(dn)
                if j < len(s.file_text[i]) - 3:
                    gridx = []
                    for k in range(i, i+4):
                        gridx.append(s.file_text[k][j:j + 4])
                    grid_found = s.check_diagonal(gridx)
            count += forward_found + grid_found

    for i in range(len(s.file_text) - 2):
        for j in range(len(s.file_text[i])-2):
            grid = [s.file_text[i][j:j + 3], s.file_text[i + 1][j:j + 3], s.file_text[i + 2][j:j + 3]]
            grid = s.filter_to_mas(grid)
            #print(grid)
            grid.sort()
            viable = [
                ['.A.', 'M.M', 'S.S'],
                ['.A.', 'M.S', 'M.S'],
                ['.A.', 'S.M', 'S.M'],
            ]
            if grid in viable:
                xcount += 1

    print(f"Part1: {count}")
    print(f"Part2: {xcount}")
if __name__ == "__main__":
    s = Solution()
    main(s)

