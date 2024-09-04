

def main():
    puzzle = get_input()

    grid = [[False for x in range(1000)] for y in range(1000)]
    for line in puzzle:
        grid = toggle_lights(grid, line)

    print(sum([sum(x) for x in grid]))

    p2_grid = [[0 for x in range(1000)] for y in range(1000)]
    for line in puzzle:
        p2_grid = adjust_brightness(p2_grid, line)

    print(sum([sum(x) for x in p2_grid]))


def toggle_lights(grid, line):

    items = line.split(' ')
    if len(items) == 5:

        start = items[2]
        end = items[4]
        new_state = True if items[1] == 'on' else False
        tog = False

    else:
        start = items[1]
        end = items[3]
        tog = True

    start = start.split(',')
    end = end.split(',')

    for i in range(int(start[0]), int(end[0])+1):
        for j in range(int(start[1]), int(end[1])+1):
            if tog:
                grid[i][j] = not grid[i][j]
            else:
                grid[i][j] = new_state

    return grid

def adjust_brightness(grid, line):
    items = line.split(' ')
    if len(items) == 5:
        start = items[2]
        end = items[4]
        adjustment = 1 if items[1] == 'on' else -1

    else:
        start = items[1]
        end = items[3]
        adjustment = 2

    start = start.split(',')
    end = end.split(',')

    for i in range(int(start[0]), int(end[0])+1):
        for j in range(int(start[1]), int(end[1])+1):
            grid[i][j] = max(0, grid[i][j] + adjustment)

    return grid

def get_input():
    with open('input.txt', 'r') as f:
        return [x.strip() for x in f.readlines()]


if __name__ == '__main__':
    main()
