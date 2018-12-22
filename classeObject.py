# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 01:28:58 2018

@author: Sharmin
"""

class Fish:
    def swim(self):
        print("fishes are swiming")
    def eat(self):
        print("Fishes are eating")

fish = Fish()
fish.swim()
fish.eat()

#Overriding Constructor
class Game:
    def __init__(self,name):
        self.name = name
    def start(self):
        print(self.name," has started")
    def stop(self):
        print(self.name," has stopped")
game = Game("Counter strike")
game.start()
game.stop()