import pygame, sys, math, random
from Player import *

class Health(pygame.sprite.Sprite):
    def __init__(self, player, pos=[0,0], tileSize = 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
       
       
        self.goodHp = pygame.transform.scale(pygame.image.load("Resources/Health/PlayerHealth/PlayerNorm.png"),  [tileSize,tileSize])        
        self.middleHp = pygame.transform.scale(pygame.image.load("Resources/Health/PlayerHealth/PlayerYellow.png"),  [tileSize,tileSize])        
        self.badHP = pygame.transform.scale(pygame.image.load("Resources/Health/PlayerHealth/PlayerLow.png"),  [tileSize,tileSize])
        
        self.hpImage = self.goodHp
        
        self.plrhp = self.Player.__init__.hp 
        
        
    def hpImag():
        if plrhp >= 60:
            self.hpImage  = self.middleHp
        if plrhp >= 30:
            self.hpImage = self.badHP
        
        
        
