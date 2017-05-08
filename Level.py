import pygame, sys, math, random
from Player import *
from Enemy1 import *
from Boss import *
from Weapons import *
from Wall import *
from Tree1 import *
from DownWall import *

class Level():
    def __init__(self, levelFile, tileSize=50):
        self.tileSize = tileSize
        self.loadLevel(levelFile)
    
    def unloadLevel(self):
        self.walls = []
        self.trees1 = []
        self.downwalls = []
        self.enemy1Spawn = []
      
               
    def loadLevel(self, levelFile):        
        f = open("Resources/levels/"+levelFile, 'r')
        lines = f.readlines()
        f.close()
        
        """
        print lines
        print "________________________"
        
        for line in lines:
            print line
        print "________________________"
        """
        newlines = []
        for line in lines:
            newline = ""
            for c in line:
                if c != '\n':
                    newline += c
            newlines += [newline]
            
        lines = newlines
        
        for line in lines:
            print line
        print "________________________"
        
        for y,line in enumerate(lines):
            for x,c in enumerate(line):
                if c == '#':
                    Wall([x*self.tileSize + self.tileSize/2,
                           y*self.tileSize + self.tileSize/2],
                          self.tileSize)
                if c == '$':
                    Tree1([x*self.tileSize + self.tileSize/2,
                           y*self.tileSize + self.tileSize/2],
                          self.tileSize)
                if c == '@':
                    DownWall([x*self.tileSize + self.tileSize/2,
                           y*self.tileSize + self.tileSize/2],
                          self.tileSize)
                if c == '&':
                    Player([x*self.tileSize + self.tileSize/2,
                           y*self.tileSize + self.tileSize/2],
                          self.tileSize)
                if c == 'E':
                    Enemy1(3,
                          [x*self.tileSize + self.tileSize/2,
                           y*self.tileSize + self.tileSize/2],
                          self.tileSize)

        
#Level("level1.lvl")
