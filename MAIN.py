import pygame, sys, math, random 
#from Boss import *
from Enemy1 import *
#from Enemy2 import *
#from Enemy3 import *
from Level import *
from Player import *               
from Wall import *
#from Weapon1 import * working on
from Tree1 import *
from DownWall import *
pygame.init()

#Before Boss1, add weapons

pygame.init()
clock = pygame.time.Clock()

width = 1200
height = 700
size = width, height 
screen = pygame.display.set_mode(size)
bgColor = r,g,b = 21, 64, 22

all = pygame.sprite.OrderedUpdates()
players = pygame.sprite.Group()
walls = pygame.sprite.Group()
enemies = pygame.sprite.Group()
#weapons1 = pyhame.sprite.Group()
 
Player.containers = all, players
Enemy1.containers = all, enemies     
Wall.containers = all, walls    
Tree1.containers = all, walls
DownWall.containers = all, walls
#Weapon1.containers = all, weapons1
level = Level("level1.lvl")

levlnum = 1   

player = players.sprites()[0]

    
bgImage = pygame.image.load("Resources/BackgroundImage/Background.png").convert()
bgRect = bgImage.get_rect()  
  
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player.go("up")
            if event.key == pygame.K_DOWN:
                player.go("down")
            if event.key == pygame.K_RIGHT:
                player.go("right")
            if event.key == pygame.K_LEFT:
                player.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                player.go("stop up")
            if event.key == pygame.K_DOWN:
                player.go("stop down")
            if event.key == pygame.K_RIGHT:
                player.go("stop right")
            if event.key == pygame.K_LEFT:
                player.go("stop left")
                    
    
    
    all.update(size)    

    playerHitsEnemy1 = pygame.sprite.spritecollide(player, enemies, True) 
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)         
    enemy1HitsWalls= pygame.sprite.groupcollide(enemies, walls, False, False)
    enemy1HitsEnemy = pygame.sprite.groupcollide(enemies, enemies, False, False)
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)
    
    for enemy in enemy1HitsWalls:
        for wall in enemy1HitsWalls[enemy]:     
            enemy.bounceWall(wall)

    for enemy1 in enemy1HitsEnemy:
        for enemy2 in enemy1HitsEnemy[enemy1]:     
            enemy1.bounceEnemy(enemy2)
        
    
      
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)











