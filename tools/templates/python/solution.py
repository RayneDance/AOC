def get_input(path="input.txt"):
    with open(path, "r") as f:
        return f.read().strip()


def part1(data: str) -> any:
    pass


def part2(data: str) -> any:
    pass


def main():
    data = get_input()
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")


if __name__ == "__main__":
    main()
