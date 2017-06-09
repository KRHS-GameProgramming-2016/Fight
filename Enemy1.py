import pygame, sys, math, random
from Player import *
#from Weapons import * working on

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, speed=0, pos=[0,0], tileSize= 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.tileSize = tileSize - 6
        self.imageLeft = pygame.image.load("Resources/EnemyImages/Enemy1/EnemyLeft1.png")
        self.imageRight = pygame.image.load("Resources/EnemyImages/Enemy1/EnemyRight1.png")
        self.imageUp = pygame.image.load("Resources/EnemyImages/Enemy1/EnemyUp1.png")
        self.imageDown = pygame.image.load("Resources/EnemyImages/Enemy1/EnemyDown1.png")

        self.imageUp = pygame.transform.scale(self.imageUp, [tileSize,tileSize])
        self.imageDown = pygame.transform.scale(self.imageDown, [tileSize,tileSize])
        self.imageRight = pygame.transform.scale(self.imageRight, [tileSize,tileSize])
        self.imageLeft = pygame.transform.scale(self.imageLeft, [tileSize,tileSize])

        self.image = self.imageRight
        self.rect = self.image.get_rect(center = pos)
        self.maxSpeed = speed
        self.enemyHealth = 100
        self.Enemy1DMG = 10
        self.enemyhp = self.enemyHealth


        self.kind = "normal"



        self.decideDirection()


        self.didBounceX = False
        self.didBounceY = False
        self.inflationTime = 0
        self.inflationLevel = 0

        self.state = "right"
        self.prevState = "right"


        self.size = tileSize
        
    def hitPlayer(self, player):
        self.enemyhp -= player.damage
        print "Enemy health", self.enemyhp
        if self.enemyhp >= 100:
            print "enemyhp > 100"
        if self.enemyhp >= 0:
            self.kill()
        
            

    
    def update(self, size):
        self.move()
        self.animate()
        self.bounceScreen(size)
        

        
        
    def move(self):
        self.didBounceX = False
        self.didBounceY = False
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        if self.speedx != 0:     #moving left/right
            if self.rect.left % self.size == 0:
                #print "left/right", self.rect.center[0]
                self.decideDirection()
        else:     #moving up/down
            if self.rect.top % self.size == 0:
            #print "left/right", self.rect.center[1]
                self.decideDirection()
        
    def decideDirection(self):
        d = random.randint(0,2)
        if d == 0: #up
            self.speedy = -self.maxSpeed
            self.speedx = 0
            self.state = "up"
        elif d == 1: #right
            self.speedx = self.maxSpeed
            self.speedy = 0
            self.state = "right"
        elif d == 2: #down
            self.speedx = 0
            self.speedy = self.maxSpeed
            self.state = "down"
        elif d == 3: #left
            self.speedx = -self.maxSpeed
            self.speedy = 0
            self.state = "left"

    def animate(self):
        if self.prevState != self.state:
            self.prevState = self.state
            if self.state == "right":
                self.image = self.imageRight
            elif self.state == "left":
                self.image = self.imageLeft
            elif self.state == "up":
                self.image = self.imageUp
            elif self.state == "down":
                self.image = self.imageDown

    def bounceWall(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.didBounceX = True
        self.didBounceY = True
        self.move()
    
    def bounceEnemy(self, other):
        if other != self:
            self.speedx = -self.speedx
            self.speedy = -self.speedy
            self.didBounceX = True
            self.didBounceY = True
            self.move()

    def bounceScreen(self, screenSize):
        screenWidth = screenSize[0]
        screenHeight = screenSize[1]
        if self.rect.top < 0 or self.rect.bottom > screenHeight:
            self.speedy = -self.speedy
        if self.rect.center[0] > screenWidth:
            self.rect.center = [0, self.rect.center[1]]
        elif self.rect.center[0] < 0:
            self.rect.center = [screenWidth, self.rect.center[1]]



    def dist(self, pt):
        x = pt[0] - self.rect.right
        y = pt[1] - self.rect.bottom
        if x < 0:
            x += -64
            x += x
        if y < 0:
            y += -64
            y += y
        return [x, y]
        return math.sqrt(xDiff**2 + yDiff**2)
        
