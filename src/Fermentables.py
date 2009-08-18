#!/bin/python

from BeerMath import *

class Fermentable:
    def __init__(self, name="Fermentable Name", type="Grain", amount=0.0, perc_yield=0.0, color="0.0"):
        self.name = name
        self.type = type
        self.amount = amount
        self.perc_yield = perc_yield
        self.color = color

