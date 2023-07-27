#!/usr/bin/python3
from dis import dis
import math


class MagicClass:
    def __init__(self, radius):
        self.__radius = 0

        # if (type(radius) is not int)
        if not type(radius, int) or not type(radius, float):
            raise TypeError('radius must be number')
        else:
            self.__radius = radius 
    
    def area(self, radius):
        return self.__radius ** 2 * math.pi
    def circumference(self, radius):
        return 2 * math.pi * self.__radius

dis(MagicClass.__init__)
