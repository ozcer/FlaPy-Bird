from src.game_object.dynamic import Dynamic


class Scenic(Dynamic):
    
    def __init__(self):
        super().__init__()
    
    
    def draw(self):
        super().draw()
    
    def update(self):
        super().update()
        
        self.x += -self.game.pan_speed
        
        if self.decayable():
            #print(f"{self} decaying")
            self.kill()
    