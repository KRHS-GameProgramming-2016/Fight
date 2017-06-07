import pygame, sys, math
#from Weapon1 import * working on
   
class Player(pygame.sprite.Sprite):
    def __init__(self, pos=[0,0], tileSize= 50):
        pygame.sprite.Sprite.__init__(self, self.containers)
        tileSize = tileSize - 6
        load = pygame.image.load
        #player health
        self.plrHPGreen = pygame.transform.scale(pygame.image.load("Resources/Health/PlayerHealth/PlayerNorm.png"),  [tileSize,tileSize])
        self.plrHPYellow = pygame.transform.scale(pygame.image.load("Resources/Health/PlayerHealth/PlayerYellow.png"),  [tileSize,tileSize])
        self.plrHPRed = pygame.transform.scale(pygame.image.load("Resources/Health/PlayerHealth/PlayerLow.png"),  [tileSize,tileSize])
        
        #No Weapon
        self.imageUpNW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithOutWeapon/PlayerUpNorm.png"),  [tileSize,tileSize])
        self.imageDownNW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithOutWeapon/PlayerDownNorm.png"),  [tileSize,tileSize])
        self.imageLeftNW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithOutWeapon/PlayerLeftNorm.png"),  [tileSize,tileSize])
        self.imageRightNW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithOutWeapon/PlayerRightNorm.png"),  [tileSize,tileSize])
        
        #Sword
        self.imageUpSW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithWeapon/PlayerSword/PlayerUpWeapon.png"),  [tileSize,tileSize])
        self.imageDownSW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithWeapon/PlayerSword/PlayerDownWeapon.png"),  [tileSize,tileSize])
        self.imageLeftSW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithWeapon/PlayerSword/PlayerLeftWeapon.png"),  [tileSize,tileSize])
        self.imageRightSW = pygame.transform.scale(pygame.image.load("Resources/PlayerImages/WithWeapon/PlayerSword/PlayerRightWeapon.png"),  [tileSize,tileSize])
        
        self.imageUp = self.imageUpNW
        self.imageDown = self.imageDownNW
        self.imageRight = self.imageRightNW
        self.imageLeft = self.imageLeftNW
        
        self.imageHPG = self.plrHPGreen
        self.imageHPY = self.plrHPYellow
        self.imageHPR = self.plrHPRed
        
        self.weapon = "none"
        
        self.hpImage = self.imageHPG
        self.image = self.imageLeft
        self.rect = self.image.get_rect(center = pos)
        self.speedx = 0
        self.speedy = 0
        self.speed = [self.speedx, self.speedy]
        self.maxSpeed = 5
        self.startPos = pos
        self.hearts = 5
        self.PHealth = 100
        self.damage = 10
        self.hp = self.PHealth
        
        
    def move(self):
        self.speed = [self.speedx, self.speedy]
        self.rect = self.rect.move(self.speed)
        
    def hitEnemy(self, enemy):   #Player lost health
        self.hp -= enemy.Enemy1DMG
        #print self.hp
        if self.hp <= 100:
            print "plr < 100"
            self.hpImage = self.imageHPG
        if self.hp <= 50:
            print "plr < 50"
            self.hpImage = self.imageHPY
        if self.hp <= 30:
            print "plr < 30"
            self.hpImage = self.imageHPR
        if self.hp <= 10:
            print "plr < 10"
            self.hpImage = self.imageHPR
        if self.hp <= 0:
            self.kill()

        
    def health(self, Enemy1):
        print "Player killed enemy"

        
    def equip(self, weapon):
        print "Weapon was touched by player"
        if weapon.kind == "sword":
            self.weapon = weapon.kind
            self.damage = weapon.damage
            self.imageUp = self.imageUpSW
            self.imageDown = self.imageDownSW
            self.imageRight = self.imageRightSW
            self.imageLeft = self.imageLeftSW
        elif weapon.kind == "axe":
            self.weapon = weapon.kind
            self.damage = weapon.damage
            self.imageUp = self.imageUpAW
            self.imageDown = self.imageDownAW
            self.imageRight = self.imageRightAW
            self.imageLeft = self.imageLeftAW
        
    def update(self, size):
        self.move()
        self.bounceScreen(size)
    
    def go(self, direction):
        if direction == "up":
            self.speedy = -self.maxSpeed
            self.image = self.imageUp
        if direction == "down":
            self.speedy = self.maxSpeed
            self.image = self.imageDown
        if direction == "left":
            self.speedx = -self.maxSpeed
            self.image = self.imageLeft
        if direction == "right":
            self.speedx = self.maxSpeed 
            self.image = self.imageRight
            
        if direction == "stop up":
            self.speedy = 0
            self.image = self.imageUp
        if direction == "stop down":
            self.speedy = 0
            self.image = self.imageDown
        if direction == "stop left":
            self.speedx = 0
            self.image = self.imageLeft
        if direction == "stop right":
            self.speedx = 0
            self.image = self.imageRight
            
    def goMouse(self, pos):
        self.rect.center = pos

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

    def bounceWall(self, other):
        self.speedx = -self.speedx
        self.speedy = -self.speedy
        self.move()
        self.speedx = 0
        self.didBounceX = True
        self.speedy = 0
        self.didBounceY = True

    
