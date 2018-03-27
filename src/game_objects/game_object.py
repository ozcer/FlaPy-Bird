import logging

from src.const import *
from src.game_objects.timers.flash import Flash
from src.gfx_helpers import *


class GameObject(pygame.sprite.Sprite):
    
    def __init__(self, game, *args,
                 pos,
                 depth,
                 init_image_key="init",
                 image_scale=(1,1),
                 ):
        """
        General game object
        :param game: Game
        :param pos: (x,y)
        :param depth: int
        :param init_image_key: key in self.images for initial image
        :param image_scale: (float x_scale, float y_scale)
        """
        super().__init__()
        self.game=game
        
        # hit box and positioning
        self.image_scale_x, self.image_scale_y = image_scale
        self.set_image_scale((self.image_scale_x, self.image_scale_y))
        
        self.x, self.y = pos
        self.image = self.images[init_image_key]
        self.rect = self.image.get_rect()
        self.rect.center = self.x, self.y
        
        # draw depth, larger=more behind
        self.depth = depth
        
        # # zone which sprites doesn't delete itself
        # self.nondecay_zone = self.game.surface.get_rect()
        
        # font for debug attributes
        self.debug_font = pygame.font.SysFont("monospace", 12)
        
        self.timers = []
        
    def update(self):
        for timer in self.timers:
            timer.update()
        self.timers = [timer for timer in self.timers if timer.duration > 0]
        
        if self.decayable():
            logging.info(f"{self} decayed")
            self.kill()
    
    def draw(self):
        self.game.surface.blit(self.image, self.rect)
        
        for timer in self.timers:
            timer.draw()
        
        if self.game.hud.dev_mode:
            self.show_attributes()
            
    def show_attributes(self):
        members = [attr for attr in dir(self)
                   if not callable(getattr(self, attr))
                   and not attr.startswith("__")]
    
        attribute_surfaces = []
        for member in members:
            attribute_surfaces.append(self.debug_font.render(f"{member}={getattr(self, member)}",
                                                   True,
                                                   GREEN)
                            )
        for index, display in enumerate(attribute_surfaces):
            self.game.surface.blit(display, (self.x, self.y + display.get_rect().h * index))

    def decayable(self):
        """
        defauls to not decay
        :return: bool
        """
        return False
    
    def collide_with_class(self, cls):
        """
        return a list of instances of the class that self is colliding with
        :param cls: class to check collision against
        :return: [pygame.sprite]
        """
        for entity in self.game.entities[GLOBAL_SPRITE_GROUP]:
            if isinstance(entity, cls) and self.rect.colliderect(entity.rect):
                logging.info(f"{self} collided with {entity}")
                return entity

    def _on_ground(self):
        # make a rect with height of 1 pixel
        # put it under the player and see if that collides with timeline
        detect_rect = pygame.Rect((0, 0), (self.rect.w, 1))
        detect_rect.top = self.rect.bottom
        
        return detect_rect.colliderect(self.game.timeline.rect)

    def _gravity(self):
        """
        affect subject with gravitational forces
        :return: None
        """
        if self.dy < MAX_DOWN_SPEED:
            self.dy += GRAV
    
    def set_image(self, new_sprite):
        """
        change sprite and recalculate rect
        :param new_sprite: Surface
        :return: None
        """
        self.image = new_sprite
        self.rect.size = self.image.get_rect().size
    
    def set_image_scale(self, image_scale):
        self.images = {name: scale_surface(image, *image_scale)
                       for (name, image) in self.images.items()}

    def draw_hitbox(self):
        pygame.draw.rect(self.game.surface, GREEN, self.rect)
    
    def overlay_color(self, color, alpha=255):
        mask = pygame.mask.from_surface(self.image)
        outline = mask.outline()
        mask_surf = pygame.Surface(self.rect.size)
        pygame.draw.polygon(mask_surf, color, outline, 0)
        mask_surf.set_colorkey((0, 0, 0))
        mask_surf.set_alpha(alpha)
        self.game.surface.blit(mask_surf, self.rect)
    
    def damaged_flash(self):
        self.timers.append(Flash(self, 500, max_alpha=100))
    
    def __str__(self):
        return f"{self.__class__.__name__} at {self.x, self.y}"