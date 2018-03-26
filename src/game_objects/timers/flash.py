from src.const import *


class Flash:
    
    def __init__(self, source, duration, color=YELLOW, max_alpha=155):
        self.source = source
        
        self.init_duration = duration
        self.duration = self.init_duration
        
        self.color = color
        self.max_alpha = max_alpha
    
    def draw(self):
        alpha = min(self.duration, self.max_alpha)
        self.source.overlay_color(self.color, alpha)
    
    def update(self):
        self.duration -= 50
