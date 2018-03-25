from src.game_objects.dynamic import Dynamic


class Scenic(Dynamic):
    
    def __init__(self, game, *, pos, depth, image):
        super().__init__(game, pos=pos, depth=depth, image=image)
    
    def decayable(self):
        """
        Overriding decayable in GameObject
        :return: bool
        """
        return self.rect.right < 0
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        self.x += -self.game.pan_speed
