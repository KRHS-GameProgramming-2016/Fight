import pygame, sys, math, random 
#from Boss import *
from Enemy1 import *
#from Enemy2 import *
#from Enemy3 import *
from Level import *
from Player import *               
from Wall import *
#from Weapons import *
from Tree1 import *
from DownWall import *
pygame.init()

   

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
enemies1 = pygame.sprite.Group()
 
Player.containers = all, players
Enemy1.containers = all, enemies1      
Wall.containers = all, walls    
Tree1.containers = all, walls
DownWall.containers = all, walls
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
                    
    
    
    all.update(size)    # Need to add into Player, Enemey and Wall sripts 

    playerHitsEnemy1 = pygame.sprite.spritecollide(player, enemies1, True) 
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)         
    enemy1HitsWalls= pygame.sprite.groupcollide(enemies1, walls, False, False)
#    EnemieshitsEnemy = pygame.sprite.groupcollide(enemies1, enemies1, False, False)
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)
    
    for wall in enemy1HitsWalls:     
        enemy.bounceWall(wall)
        

      
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)











