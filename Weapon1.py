import pygame, sys, math, random
from Player import *
from Enemy1 import *


class BasicSword(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], tileSize= 25):
        pygame.sprite.Sprite.__init__(self, self.containers)
        tileSize = tileSize - 6
        load = pygame.image.load
        self.imageUp = load("")
        self.imageDown = load("")   #Make BasicSword images 
        self.imageLeft = load("")
        self.imageRight = load("")
        self.imageUp = pygame.transform.scale(self.imageUp, [tileSize,tileSize])
        self.imageDown = pygame.transform.scale(self.imageDown, [tileSize,tileSize])
        self.imageRight = pygame.transform.scale(self.imageRight, [tileSize,tileSize])
        self.imageLeft = pygame.transform.scale(self.imageLeft, [tileSize,tileSize])
        self.image = self.imageLeft
        self.rect = self.image.get_rect(center = pos)
        
        
        
    def swordDmg(self):
        
        
    
        
        
    
        
