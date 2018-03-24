import pygame


def scale_surface(surface, x_scale, y_scale):
    """
    scale surface around surface.rect.center
    :param surface: Surface to scale
    :param x_scale: int: 1 = 100%
    :param y_scale: int: 1 = 100%
    :return: scaled Surface
    """
    image_rect = surface.get_rect()
    delta_x = image_rect.right * (x_scale - 1)
    delta_y = image_rect.bottom * (y_scale - 1)
    scaled_rect = image_rect.inflate(delta_x, delta_y)
    result = pygame.transform.scale(surface, scaled_rect.size)
    return result
