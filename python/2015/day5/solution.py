
def main():
    strings = get_input()
    nice_strings = 0

    for string in strings:
        if is_nice(string):
            nice_strings += 1

    p2 = 0
    for string in strings:
        if p2_is_nice(string):
            p2 += 1

    print(nice_strings)
    print(p2)


def is_nice(string):
    vowels = "aeiou"
    bad_strings = ["ab", "cd", "pq", "xy"]
    vowels_count = 0
    double_letter = False

    for i in range(len(string)):
        if 0 < i < len(string):
            sub = string[i-1:i+1]
            if sub in bad_strings:
                return False
            if sub[0] == sub[1]:
                double_letter = True
        if string[i] in vowels:
            vowels_count += 1

    if vowels_count < 3 or not double_letter:
        return False
    return True


def p2_is_nice(string):
    pair = False
    repeat = False

    for i, c in enumerate(string):
        if i+1 < len(string):
            if string[i:i+2] in string[i+2:]:
                pair = True
        if i+2 < len(string):
            if c == string[i+2]:
                repeat = True

    if pair and repeat:
        return True
    return False


def get_input():
    with open("input.txt", "r") as f:
        return f.read().splitlines()

if __name__ == "__main__":
    main()