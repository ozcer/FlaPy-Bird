from src.game_object.dynamic import Dynamic


class Scenic(Dynamic):
    
    def __init__(self, game, *, pos, depth, image):
        super().__init__(game, pos=pos, depth=depth, image=image)

    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        self.x += -self.game.pan_speed
        
        if self.decayable():
            self.kill()
