
def main():
    xy = [0, 0]
    visited = set()
    visited.add((0, 0))

    for direction in get_input():
        dx, dy = match_direction(direction)
        xy[0] += dx
        xy[1] += dy

        visited.add(tuple(xy))

    print("Part 1: ", len(visited))

    santa_xy = [0, 0]
    robo_xy = [0, 0]
    visited = set()
    visited.add((0, 0))

    for i, direction in enumerate(get_input()):
        xy = santa_xy if i % 2 == 0 else robo_xy
        dx, dy = match_direction(direction)
        xy[0] += dx
        xy[1] += dy

        if i % 2 == 0:
            santa_xy = xy
        else:
            robo_xy = xy

        visited.add(tuple(xy))

    print("Part 2: ", len(visited))

def match_direction(direction):
    match direction:
        case '^':
            return (0, 1)
        case 'v':
            return (0, -1)
        case '>':
            return (1, 0)
        case '<':
            return (-1, 0)
        case _:
            print('Invalid direction')
            return (0, 0)

def get_input():
    with open('input.txt', 'r') as f:
        return f.read().strip()


if __name__ == '__main__':
    main()