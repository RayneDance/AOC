from enum import Enum
import copy

class Solution:
    def __init__(self):
        self.file_text = open("example.txt", "r").readlines()
        self.board = []
        self.player = Player((0, 0))
        self.path = set()
        self.last_run = False

        for i, line in enumerate(self.file_text):
            line = line.strip()
            self.board.append([])
            for j, char in enumerate(line):
                match char:
                    case '.':
                        self.board[-1].append(GameObject((j, i)))
                    case '#':
                        self.board[-1].append(GameObject((j, i), False))
                    case '^':
                        self.board[-1].append(GameObject((j, i)))
                        self.player.set_location((j, i))
                        self.player.origin = (j, i)


    def generate_map(self):
        next_pos = self.navigate_board()
        self.player.moves.add(next_pos)

        while next_pos:
            next_pos = self.navigate_board()
            if next_pos:
                self.player.moves.add(next_pos)
        self.path = self.player.moves.copy()

    def navigate_board(self):
        ppos = self.player.get_location()
        next_pos = ppos[0] + self.player.direction.value[0], ppos[1] + self.player.direction.value[1]

        if not (0 <= next_pos[1] < len(self.board) and 0 <= next_pos[0] < len(self.board[0])):
            return False

        for _ in range(4):  # Check all four directions
            if self.board[next_pos[1]][next_pos[0]].passable:
                break
            self.player.next_direction()
            next_pos = (self.player.get_location()[0] + self.player.direction.value[0],
                        self.player.get_location()[1] + self.player.direction.value[1])
        else:
            return False


        self.player.set_location(next_pos)
        return next_pos

    def run_new_board(self):
        next_pos = self.navigate_board()
        self.player.path.append(next_pos)
        search_control = 0
        while next_pos:
            next_pos = self.navigate_board()
            if next_pos:
                self.player.path.append(next_pos)
                if search_control % 100 == 0:
                    if self.check_path_for_loop():
                        self.last_run = True
                        return
                search_control += 1

    def check_path_for_loop(self):
        if len(self.player.path) > len(self.board) * len(self.board):
            return True
        return False

    def return_to_origin(self):
        self.player.set_location(self.player.origin)
        self.player.path.clear()
        self.player.moves.clear()

class Directions(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class GameObject:
    def __init__(self, coordinates, passable=True):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.passable = passable


class Player(GameObject):
    def __init__(self, coordinates):
        super().__init__(coordinates, False)
        self.direction = Directions.UP
        self.moves = set()
        self.path = []
        self.origin = None

    def set_location(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]

    def get_location(self):
        return self.x, self.y

    def record_move(self, location):
        self.moves.add(location)

    def next_direction(self):
        match self.direction:
            case Directions.UP:
                self.direction = Directions.RIGHT
            case Directions.RIGHT:
                self.direction = Directions.DOWN
            case Directions.DOWN:
                self.direction = Directions.LEFT
            case Directions.LEFT:
                self.direction = Directions.UP

def print_board(board):
    print("_______BOARD_______")
    local_board = []
    for i, line in enumerate(board):
        local_board.append([])
        for j, item in enumerate(line):
            match item.passable:
                case True:
                    local_board[-1].append(".")
                case False:
                    local_board[-1].append("#")
    for line in local_board:
        print("".join(line))

def main():
    s = Solution()
    s.generate_map()
    p1_count = len(s.path)
    print(f"Part 1: {p1_count}")

    main_board = copy.deepcopy(s.board)
    s.path.remove((s.player.origin[0], s.player.origin[1]-1))
    #s.path.remove(s.player.origin)
    p2_count = 0

    for item in s.path:
        s.return_to_origin()
        s.player.direction = Directions.UP
        s.board[item[1]][item[0]] = GameObject(item, False)
        s.run_new_board()
        if s.last_run:
            p2_count += 1
            s.last_run = False
        s.board = copy.deepcopy(main_board)
        s.player.path.clear()
    print(f"Part 2: {p2_count}")


if __name__ == "__main__":
    main()