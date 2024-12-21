
class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.file_text = [x.strip() for x in self.file_text]
        self.pairs = [t for t in self.file_text if t.count("|") == 1]
        self.lists = [t for t in self.file_text if t.count("|") != 1]
        self.lists = [[x for x in t.split(",")] for t in self.lists if t != '']


def main():
    s = Solution()
    rule_pairs = {}


    for pair in s.pairs:
        left, right = pair.split("|")
        left = left.strip()
        right = right.strip()
        if left not in rule_pairs:
            rule_pairs[left] = []
        rule_pairs[left].append(right)
        if right not in rule_pairs:
            rule_pairs[right] = []


    alt_mid = 0
    for l in s.lists:
        for i in range(len(l)-1, -1, -1):
            fail = False
            for j in range(i-1, -1, -1):
                if l[j] in rule_pairs[l[i]]:
                    fail = True
                    break
            if fail:
                break
        else:
            alt_mid += int(l[len(l) // 2])

    midp2 = 0
    for l in s.lists:
        incorrect = False
        i = len(l) - 1
        while i >= 0:
            fail = False
            j = i-1
            for j in range(i-1, -1, -1):
                if l[j] in rule_pairs[l[i]]:
                    incorrect = True
                    l[i], l[j] = l[j], l[i]
                    i += 1
                    break
            i -= 1
        if incorrect:
            midp2 += int(l[len(l) // 2])

    print(alt_mid, midp2)

if __name__ == "__main__":
    main()