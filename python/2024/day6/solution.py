import pygame
from screen import Screen
from gameobj import GameObject, Directions, EntityTypes

class Solution:
    def __init__(self):
        self.file_text = open("input.txt", "r").readlines()

def main():
    s = Solution()
    objects = []
    board = []
    player = None
    board_w = len(s.file_text[0])
    board_h = len(s.file_text)
    config = {}
    config["background"] = (255, 255, 255)
    config["screen_size"] = (1000, 1000)
    config["ui_area"] = (0, 0, 0, 0)
    config["piece_size"] = [config["screen_size"][0]//(len(s.file_text[0])), (config["screen_size"][1])//(len(s.file_text))]
    config["screen_size"] = (config["piece_size"][0]*len(s.file_text[0]), config["piece_size"][1]*len(s.file_text))
    config["tail_color"] = (50, 200, 50)
    screen = Screen(config)
    print(config["piece_size"])



    for i, line in enumerate(s.file_text):
        board.append([])
        for j, char in enumerate(line):
            if char == "\n":
                continue
            objects.append(GameObject((j, i), piece=char))
            board[i].append(objects[-1])
            if char == "^":
                player = objects[-1]
    can_continue = True
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        #pygame.time.wait(50)
        pygame.display.set_caption(f"Unique positions visited: {len(player.moves)+1}")

        new_pos = player.location[0] + player.direction.value[0], player.location[1] + player.direction.value[1]
        try:
            new_loc_obj = board[new_pos[1]][new_pos[0]]
        except IndexError:
            can_continue = False

        if can_continue:
            if new_loc_obj.type == EntityTypes.WALL:
                #print("Wall ahead!")
                match player.direction:
                    case Directions.UP:
                        player.direction = Directions.RIGHT
                    case Directions.RIGHT:
                        player.direction = Directions.DOWN
                    case Directions.DOWN:
                        player.direction = Directions.LEFT
                    case Directions.LEFT:
                        player.direction = Directions.UP

                new_pos = player.location[0] + player.direction.value[0], player.location[1] + player.direction.value[1]
                new_loc_obj = board[new_pos[1]][new_pos[0]]
                new_loc_obj.color = config["tail_color"]
            else:
                new_loc_obj.color = config["tail_color"]
            player.move()

        screen.draw(objects)



if __name__ == "__main__":
    main()