import pygame
from pygame.sprite import collide_mask

class DoesCollide:

    def collideLeft(rect, objects):
        collisions = 0
        for object in objects:
            if rect.midleft == object.midright:
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False

    def collideRight(rect, objects):
        collisions = 0
        for object in objects:
            if rect.midright == object.midleft:
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False

    def collideBottom(rect, objects):
        collisions = 0
        for object in objects:
            if rect.midbottom == object.midtop:
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False

    def collideTop(rect, objects):
        collisions = 0
        for object in objects:
            if rect.midtop == object.midbottom:
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False