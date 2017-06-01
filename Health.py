import pygame, sys, math, random
from Player import *
from Enemy1 import *
from Weapon1 import *

class Health():
    def __init__(self, player, pos=[0,0], path = "Resources/Health/"):
        self.playerHealth = 100
        self.enemy1Health = 100
        self.enemy2Health = 200
        
        self.enemy1DMG = 10
        self.enemy2DMG = 20
        
