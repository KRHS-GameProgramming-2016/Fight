import pygame, sys, math

class Player():
    def __init__(self, pos=[0,0], tileSize= 50):
        load = pygame.image.load
        self.imageUp = load("Resources/")
        self.imageDown = load("")
        self.imageleft = load("")
        self.imageRight = load("")
        
        
        #           -- Make sure to add sprite.collide with the enemy, boss and wall. 
        #           -- Need to add collide with the wall. 
    
