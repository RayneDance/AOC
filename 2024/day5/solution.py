class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.file_text = [x.strip() for x in self.file_text]
        self.raw_pairs = [t for t in self.file_text if t.count("|") == 1]
        self.lists = [t for t in self.file_text if t.count("|") != 1]
        self.lists = [t for t in self.lists if t != '']
        self.pairs = [t.split("|") for t in self.raw_pairs]
        self.pairs = [Node(x[0], Node(x[1])) for x in self.pairs]

class Node:
    def __init__(self, val, children=None):
        self.value = val
        self.children = []
        if children:
            self.children = children
    def __repr__(self):
        if not self.children:
            return f"Node({self.value})\n"
        else:
            return f"Node({self.value})\n{self.children}"

def main():
    s = Solution()



def DFS(node, s):
    if node.value == s.value:
        return node

    for child in node.children:
        result = DFS(child, s)
        if result:
            return result
    return None


if __name__ == "__main__":
    main()