from enum import Enum

class EntityTypes(Enum):
    TRAVERSE = "."
    WALL = "#"
    PLAYER = "^"

class Directions(Enum):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)

class GameObject:
    def __init__(self, location: tuple, color=None, z_index=0, piece=None):
        self.location = location
        self.direction = Directions.UP
        self.color = color if color else (173, 216, 230)
        self.z_index = z_index if z_index else 0
        self.render = True
        self.type = None
        self.moves = set()

        match piece:
            case '.':
                self.type = EntityTypes.TRAVERSE
                self.color = (255, 255, 255)
            case '#':
                self.type = EntityTypes.WALL
                self.color = (255, 0, 0)
            case '^':
                self.type = EntityTypes.PLAYER
                self.color = (0, 255, 0)
                self.z_index = 5

    def move(self):
        self.location = (self.location[0] + self.direction.value[0], self.location[1] + self.direction.value[1])
        self.moves.add(self.location)