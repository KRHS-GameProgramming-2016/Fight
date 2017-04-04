import pygame, sys, math

class Player():
    def __init__(self, pos=[0,0], tileSize= 50):
        load = pygame.image.load
        self.imageUp = load("Resources/PlayerImages/WithOutWeapon/PlayerUpNorm.png")
        self.imageDown = load("Resources/PlayerImages/WithOutWeapon/PlayerDownNorm.png")   #The player loads with weapon
        self.imageleft = load("Resources/PlayerImages/WithOutWeapon/PlayerLeftNorm.png")
        self.imageRight = load("Resources/PlayerImages/WithOutWeapon/PlayerRightNorm.png")
        
        
        #           -- Make sure to add sprite.collide with the enemy, boss and wall. 
        #           -- Need to add collide with the wall. 
    
