import pygame, sys, math, random
from Player import *
from Enemy1 import *


class Weapon1(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], tileSize= 15):
        pygame.sprite.Sprite.__init__(self, self.containers)
        tileSize = tileSize - 6
        load = pygame.image.load
        self.image = load("Resources/WeaponImages/BasicSword.png")
        self.image = pygame.transform.scale(self.image, [tileSize,tileSize])
        self.image = self.image
        self.rect = self.image.get_rect(center = pos)
        
        
        
        
        
    
        
        
    
        
