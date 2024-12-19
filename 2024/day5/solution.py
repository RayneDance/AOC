
class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.file_text = [x.strip() for x in self.file_text]
        self.pairs = [t for t in self.file_text if t.count("|") == 1]
        self.lists = [t for t in self.file_text if t.count("|") != 1]
        self.lists = [[x for x in t.split(",")] for t in self.lists if t != '']

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []

    def __repr__(self):
        return self.val

    def deep_child(self, val, seen_items=None):
        if seen_items is None:
            seen_items = set()
            seen_items.add(self.val)
        else:
            if self.val in seen_items:
                return False
            else:
                seen_items.add(self.val)
        for child in self.children:
            if val == child.val:
                return True
            else:
                if child.deep_child(val, seen_items):
                    return True
        return False
def main():
    s = Solution()
    nodes = {}

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

        if left not in nodes:
            nodes[left] = Node(left)
        if right not in nodes:
            nodes[right] = Node(right)
        nodes[left].children.append(nodes[right])

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

    mid_count = 0
    for l in s.lists:
        for i in range(len(l)-1):
            if not nodes[l[i]].deep_child(l[i+1]):
                break
        else:
            mid_count += int(l[len(l)//2])
    print(alt_mid)

if __name__ == "__main__":
    main()