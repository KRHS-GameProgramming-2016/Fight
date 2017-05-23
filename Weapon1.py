import pygame, sys, math, random

class Sword(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.image.load("Resources/WeaponImages/BasicSword.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.kind = "sword"
        self.damage = 50

class Axe(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], size=None):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.image = pygame.image.load("Resources/WeaponImages/Axe.png")
        if size:
            self.image = pygame.transform.scale(self.image, [size,size])
        self.rect = self.image.get_rect(center = pos)
        self.kind = "axe"
        self.damage = 65
        
