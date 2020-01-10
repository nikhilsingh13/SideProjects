# -*- coding: utf-8 -*-
"""
Created on Sat Nov  13 2019
@filename: inventory.py
@author: Nikhil Singh
"""

class Item:
    def __init__(self, name, type, description, prop):
        self.name = name
        self.type = type
        self.description = description
        self.prop = prop
        