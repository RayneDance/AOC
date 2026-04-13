import pygame


class Screen:
    def __init__(self, config):
        self.config = config
        self.surface = pygame.display.set_mode(self.config["screen_size"])

    def draw(self, gameobjs: list):
        self.surface.fill(self.config["background"])
        new_gameobjs = sorted(filter(lambda x: x.render, gameobjs), key=lambda x: x.z_index)
        for gameobj in new_gameobjs:
            if gameobj.render:
                x = gameobj.location[0] * self.config["piece_size"][0]
                y = gameobj.location[1] * self.config["piece_size"][1]
                w = self.config["piece_size"][0]
                h = self.config["piece_size"][1]
                pygame.draw.rect(self.surface,
                                 gameobj.color,
                                 [x, y, w, h]
                                 )
        pygame.display.flip()