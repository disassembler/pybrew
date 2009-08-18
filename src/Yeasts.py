#!/bin/python

from BeerMath import *

class Yeast:
    def __init__(self, name="Yeast Name", type="Ale", form="Dry" amount=0.0, notes="Yeast Description"):
        self.name = name
        self.type = type
        self.form = form
        self.amount = amount
        self.notes = notes

