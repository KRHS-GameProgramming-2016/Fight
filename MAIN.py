import pygame, sys, math, random 
#from Boss import *
#from Enemy import *
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
trees1 = pygame.sprite.Group()
downwalls = pygame.sprite.Group()
 
Player.containers = all, players
#Enemy.containers = all, enemies      -- Will add after the main part of the game is done
Wall.containers = all, walls    
Tree1.containers = all, trees1
DownWall.containers = all, downwalls
level = Level("level1.lvl")

levlnum = 1   

player = Player.containers
    
    
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                players.go("up")
            if event.key == pygame.K_DOWN:
                players.go("down")
            if event.key == pygame.K_RIGHT:
                players.go("right")
            if event.key == pygame.K_LEFT:
                players.go("left")
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                players.go("stop up")
            if event.key == pygame.K_DOWN:
                players.go("stop down")
            if event.key == pygame.K_RIGHT:
                players.go("stop right")
            if event.key == pygame.K_LEFT:
                players.go("stop left")
        else:
            if event.type == pygame.MOUSEMOTION:
                pygame.mouse.set_visible(False)
                players.goMouse(event.pos)
                    
    bgImage = pygame.image.load("Resources/BackgroundImage/Background.png").convert()
    bgRect = bgImage.get_rect()
    all.update(size)    # Need to add into Player, Enemey and Wall sripts 

    #playerHitsEnemy = pygame.sprite.spritecollide(player, enemies, True) 
    playerHitsWalls = pygame.sprite.spritecollide(player, walls, False)         
    #enemyHitsWalls= pygame.sprite.groupcollide(enemies, walls, False, False)
    #EnemieshitsEnemy = pygame.sprite.groupcollide(balls, balls, False, False)
    
    bgColor = r,g,b
    screen.fill(bgColor)
    screen.blit(bgImage, bgRect)
    dirty = all.draw(screen)
    pygame.display.update(dirty)
    pygame.display.flip()
    clock.tick(60)











