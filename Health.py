import pygame, sys, math, random
from Player import *
from Enemy1 import *
from Weapon1 import *

class Health():
    def __init__(self, player, pos=[0,0], path = "Resources/Health/"):
        
