from enum import Enum

class Direction(Enum):
    UP = (-1, 0)
    DOWN = (1, 0)
    LEFT = (0, -1)
    RIGHT = (0, 1)

class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()
        self.board = [[int(x) for x in line.strip()] for line in self.file_text]
        self.nodes = []
        for i in range(len(self.file_text)):
            for j in range(len(self.file_text[i])):
                if self.file_text[i][j] == "0":
                    self.nodes.append(Node(0, (i, j)))
        self.build_graphs()

        total = 0
        total2 = 0
        for node in self.nodes:
            nines, count = self.count_paths_to_top(node)
            total += len(nines)
            total2 += count
        print(total, total2)

    def build_graphs(self):
        for node in self.nodes:
            self.crawl_children(node)

    def crawl_children(self, node):
        self.get_surroundings(node)
        for child in node.children:
            self.crawl_children(child)

    def count_paths_to_top(self, node):
        locations = set()
        count = 0
        if node.value == 9:
            count = 1
            locations.add(node.location)
        else:
            for child in node.children:
                res, new_count = self.count_paths_to_top(child)
                count += new_count
                locations.update(res)
        return locations, count


    def get_surroundings(self, node):
        #check bounds then process
        up = (Direction.UP.value[0] + node.location[0], Direction.UP.value[1] + node.location[1])
        down = (Direction.DOWN.value[0] + node.location[0], Direction.DOWN.value[1] + node.location[1])
        right = (Direction.RIGHT.value[0] + node.location[0], Direction.RIGHT.value[1] + node.location[1])
        left = (Direction.LEFT.value[0] + node.location[0], Direction.LEFT.value[1] + node.location[1])
        if not up[0] < 0:
            if self.board[up[0]][up[1]] == node.value + 1:
                node.children.append(Node(self.board[up[0]][up[1]], up))
        if not down[0] >= len(self.board):
            if self.board[down[0]][down[1]] == node.value + 1:
                node.children.append(Node(self.board[down[0]][down[1]], down))
        if not right[1] >= len(self.board[0]):
            if self.board[right[0]][right[1]] == node.value + 1:
                node.children.append(Node(self.board[right[0]][right[1]], right))
        if not left[1] < 0:
            if self.board[left[0]][left[1]] == node.value + 1:
                node.children.append(Node(self.board[left[0]][left[1]], left))



class Node:
    def __init__(self, value, location):
        self.value = value
        self.location = location
        self.children = []

    def __repr__(self):
        return f"Node({self.value}, {self.location}, {self.children})"

def main():
    s = Solution()

if __name__ == "__main__":
    main()