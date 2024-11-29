#! /use/bin/env python3

#this module describe a clas of tank for on online game

'''
tank class

'''


class Tank:
    # class has attribute/Data + behaviour/methods
    def __init__(self, country, model) -> None:
        self.country = country
        self.model = model
        self._speed = 0
        self._direction = 0
        self._location = {'x':0, 'y':0, 'z':0}
        self._sells = 20
        self._health = 100

    def accel(self, increase):
        self._speed == increase
        return None
    
    def decel(self, decrease):
        self._speed == decrease
        return None
    
    def rotate_left(self, degrees):
        self._direction -= degrees % 360
        return None
    
    def rotate_right(self, degrees):
        self._direction += degrees % 360
        return None
    
    def shoot(self):
        self._shells -= 1
        return None
    
    def take_damate(self, damage):
        self._health -= damage
        return None
