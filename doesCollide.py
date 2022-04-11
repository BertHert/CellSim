import pygame
from pygame.sprite import collide_mask

class DoesCollide:

    def collideLeft(rect, objects):
        collisions = 0
        for object in objects:
            if object.collidepoint(rect.midleft[0], rect.midleft[1]):
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False

    def collideRight(rect, objects):
        collisions = 0
        for object in objects:
            if object.collidepoint(rect.midright[0], rect.midright[1]):
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False

    def collideBottom(rect, objects):
        collisions = 0
        for object in objects:
            if object.collidepoint(rect.midbottom[0], rect.midbottom[1]):
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False

    def collideTop(rect, objects):
        collisions = 0
        for object in objects:
            if object.collidepoint(rect.midtop[0], rect.midtop[1]):
                collisions += 1
        if (collisions > 0):
            return True
        else:
            return False