
def main():
    # Day 1
    # Part 1

    puz = get_input()

    nums = [1 if x == "(" else -1 for x in puz]
    print("Part 1:", sum(nums))

    hold = 0
    for i, num in enumerate(nums):
        hold += num
        if hold == -1:
            print("Part 2:", i + 1)
            break

def get_input():
    with open("input.txt", "r") as f:
        return f.read().strip()


if __name__ == "__main__":
    main()