# -*- coding: utf-8 -*-
"""
Created on Sat Nov  12 2019
@filename: enemy.py
@author: Nikhil Singh
"""

class Enemy:
    def __init__(self, hp, mp):
        self.max_hp=hp
        self.hp=hp
        
        self.max_mp=mp
        self.mp=mp
        
    def get_hp(self):
        return self.hp