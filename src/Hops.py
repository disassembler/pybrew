#!/bin/python

from BeerMath import *

class Hop:
    def __init__(self, name="Hop Name", alpha=0.0, amount=0.0, notes="Hop Description", form="Pellet"):
        self.name = name
        self.alpha = alpha
        self.amount = amount
        self.notes = notes
        self.form = form

