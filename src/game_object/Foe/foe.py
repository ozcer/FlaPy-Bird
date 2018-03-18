from src.const import *
from src.game_object.dynamic import *

class Foe(Dynamic):
    depth = -4
    def __init__(self, game, image):
        super().__init__()
        self.game = game

        #Starting Position
        self.x = DISPLAY_WIDTH + 50
        self.y = DISPLAY_HEIGHT/2

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.width = self.rect.width
        self.height = self.rect.height

        #life state
        self.alive = True

    def draw(self):
        super().draw()

    def update(self):
        self.x += self.dx
        self.y += self.dy
        self.rect.center = self.x, self.y
