from src.game_object.dynamic import Dynamic

class Foe(Dynamic):
    def __init__(self,
                 game,
                 pos,
                 depth,
                 image):
        super().__init__()

        self.game = game

        #Sprite
        self.depth = depth
        self.image = image

        #Starting Position
        self.x, self.y = pos

        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        self.width = self.rect.width
        self.height = self.rect.height

        #life state
        self.alive = True

    def draw(self):
        super().draw()

    def update(self):
        super().update()

        #health condition
        if self.hp is 0 or self.decayable():
            self.alive = False

        if not self.alive:
            self.kill()



