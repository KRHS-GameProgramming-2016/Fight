import pygame, sys, math, random 
#from Boss import *
from Enemy1 import *
#from Enemy2 import *
#from Enemy3 import *
from Level import *
from Player import *               
from Wall import *
from Weapon1 import * 
from Tree1 import *
from DownWall import *
from Goal import *
#from Health import * 
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
weapons = pygame.sprite.Group()
goals = pygame.sprite.Group()
#healths = pygame.sprite.Group()
 
Player.containers = all, players
Enemy1.containers = all, enemies     
Wall.containers = all, walls    
Tree1.containers = all, walls
DownWall.containers = all, walls
Sword.containers = all, weapons
Goal.containers = all, goals
#Health.containers = all, healths
level = Level("level1.lvl")

levelNumber = 1   


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
    

    playerHitsEnemy = pygame.sprite.spritecollide(player, enemies, False), 
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)         
    enemy1HitsWalls= pygame.sprite.groupcollide(enemies, walls, False, False)
    enemy1HitsEnemy = pygame.sprite.groupcollide(enemies, enemies, False, False)
    playerHitgoals = pygame.sprite.spritecollide(player, goals, False) 
    playerHitsWeapon = pygame.sprite.spritecollide(player, weapons, True)
    
    for weapon in playerHitsWeapon:
        player.equip(weapon)
        
    for enemy in playerHitsEnemy[0]: #playerHitsEnemy is returning a tuple...this is an ugly fix that might break at some point and who knows how
        player.health(player)
        player.hitEnemy(enemy)
        enemy.hitPlayer(player)
        
        #health sub
    
    for wall in playerHitsWalls:
        player.bounceWall(wall)
    
    for enemy in enemy1HitsWalls:
        for wall in enemy1HitsWalls[enemy]:     
            enemy.bounceWall(wall)

    for enemy1 in enemy1HitsEnemy:
        for enemy2 in enemy1HitsEnemy[enemy1]:     
            enemy1.bounceEnemy(enemy2)
            
    for goal in playerHitgoals:
        level.unloadLevel(all)
        levelNumber += 1
        level = Level("level" + str(levelNumber) + ".lvl")
        player = players.sprites()[0]

            
    
      
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)











