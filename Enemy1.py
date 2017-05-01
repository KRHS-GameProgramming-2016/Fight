import pygame, sys, math, random
from Weapons import *

class Enemy1(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], tileSize=50, speed=5):
        load = pygame.image.load
        self.imageUp = load("Resources/EnemyImages/Enemy1/EnemyUp1.png")
        self.imageDown = load("Resources/EnemyImages/Enemy1/EnemyDown1.png")   
        self.imageLeft = load("Resources/EnemyImages/Enemy1/EnemyLeft1.png")
        self.imageRight = load("Resources/EnemyImages/Enemy1/EnemyRight1.png")
        self.imageUp = pygame.transform.scale(self.imageUp, [tileSize,tileSize])
        self.imageDown = pygame.transform.scale(self.imageDown, [tileSize,tileSize])
        self.imageRight = pygame.transform.scale(self.imageRight, [tileSize,tileSize])
        self.imageLeft = pygame.transform.scale(self.imageLeft, [tileSize,tileSize])
        self.image = self.imageLeft
        self.rect = self.image.get_rect(center = pos)
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = speed
        
        print pos
        print speed

        self.kind = "normal"

        self.decideDirection()


        self.didBounceX = False
        self.didBounceY = False
        self.inflationTime = 0
        self.inflationLevel = 0

        self.state = "right"
        self.prevState = "right"
        
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
        self.animate()

    def decideDirection(self):
        d = random.randint(0,2)
        if d == 0: #up
            self.speedx = 0
            self.speedy = -self.maxSpeed
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
        self.move()
        self.speedx = 0
        self.didBounceX = True      #Already added on main 
        self.speedy = 0
        self.didBounceY = True


    def bounceScreen(self, size):
        width = size[0]
        height = size[1]
        if self.rect.left < 0 or self.rect.right > width:
            self.speedx = -self.speedx
            self.move()
            self.speedx = 0
            self.didBounceX = True
        if self.rect.top < 0 or self.rect.bottom > height:
            self.speedy = -self.speedy
            self.move()
            self.speedy = 0
            self.didBounceY = True



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
