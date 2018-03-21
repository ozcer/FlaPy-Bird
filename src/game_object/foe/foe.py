import pygame

from src.game_object.dynamic import Dynamic


class Foe(Dynamic):

    def __init__(self,
                 game, *,
                 pos,
                 depth=-4,
                 image):
        super().__init__(game, pos=pos, depth=depth, image=image)

        # life state
        self.alive = True
    
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

        # health condition
        if self.hp is 0:
            self.alive = False

        if not self.alive:
            self.kill()



