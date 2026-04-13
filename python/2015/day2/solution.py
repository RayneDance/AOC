
def main():
    lines = get_input()
    total_paper = 0

    for line in lines:
        dimensions = [int(x) for x in line.strip().split('x')]
        total_paper += calc_paper(dimensions)

    print("Part 1:", total_paper)

    total_ribbon = 0
    for line in lines:
        dimensions = [int(x) for x in line.strip().split('x')]
        total_ribbon += calc_ribbon(dimensions)

    print("Part 2:", total_ribbon)


def calc_ribbon(dimensions):
    dimensions.sort()
    return 2 * (dimensions[0] + dimensions[1]) + (dimensions[0] * dimensions[1] * dimensions[2])


def calc_paper(dimensions):
    l, w, h = dimensions
    side1 = l * w
    side2 = w * h
    side3 = h * l

    return 2 * (side1 + side2 + side3) + min(side1, side2, side3)


def get_input():
    with open('input.txt', 'r') as f:
        return f.readlines()


if __name__ == '__main__':
    main()