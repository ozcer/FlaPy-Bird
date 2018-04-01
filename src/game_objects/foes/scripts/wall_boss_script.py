from src.const import *
from src.game_objects.wall import Wall


class WallBossScript:
    
    def __init__(self, speed, dest_x):
        self.speed = speed
        self.dest_x = dest_x
        self.wall_cd = 0
        
    def update(self):
        if self.host.x > self.dest_x:
            self.host.dx = -self.speed
        else:
            self.host.dx = 0

        self.wall_cd -= 1
        if self.wall_cd <= 0:
            self.make_walls()
            self.wall_cd = WALL_RATE

    def make_walls(self):
        wall_height = 100
        wall = Wall(self.host.game,
                    pos=(self.host.x, self.host.y),
                    dim=(WALL_WIDTH, wall_height))
        self.host.game.add_entity(wall)