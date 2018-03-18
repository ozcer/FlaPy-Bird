from src.game_object.Foe.foe import *
import random

class BasicFoe(Foe):
    def __init__(self, game):
        #Sprite
        self.sprites = {"ooze": pygame.image.load("sprites/foesprites/foe1.png"),
                        "tedders": pygame.image.load("sprites/foesprites/foe2.png")}
        self.image = random.choice(list(self.sprites.items()))[1]

        #Movement
        self.dx = -1
        self.dy = 0

        #Monster Hp
        self.life = 50
        super().__init__(game, self.image)

    def draw(self):
        Foe.draw(self)

    def update(self):
        Foe.update(self)
