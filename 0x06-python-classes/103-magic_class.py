#!/usr/bin/python3
"""
This module defines a MagicClass that represents a circle with a given radius.
"""
import math


class MagicClass:
    """
    A class that represents a circle with a given radius.
    """
    def __init__(self, radius=0):
        """
        Initializes the MagicClass object with the given radius.
        Raises a TypeError if the radius is not a number.

        Args:
            radius (float): The radius of the circle.
        """
        self.__radius = 0
        if type(radius) not in [int, float]:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self) -> float:
        """
        Returns the area of the circle.
        """
        return self.__radius ** 2 * math.pi

    def circumference(self) -> float:
        """
        Returns the circumference of the circle.
        """
        return 2 * math.pi * self.__radius
