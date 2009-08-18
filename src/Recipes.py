#!/bin/python

from BeerMath import *
from Hops import Hop
from Fermentables import Fermentable
from Yeasts import Yeast

class Recipe:
    def __init__(self, name="Recipe Name", type="All Grain", brewer="Anonymous", batch_size=18.927, boil_size=22.712, boil_time=60):
        self.name = name
        self.type = type
        self.brewer = brewer
        self.batch_size = batch_size
        self.boil_size = boil_size
        self.boil_time = boil_time

