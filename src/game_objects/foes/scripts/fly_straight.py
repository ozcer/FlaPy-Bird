from src.const import *

class FlyStraight:
    
    def __init__(self, speed):
        self.speed = speed
    
    def update(self):
        self.host.dx = -self.speed
