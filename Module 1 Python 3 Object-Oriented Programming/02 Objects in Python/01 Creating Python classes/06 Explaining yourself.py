import math

class Point:
    'Represents a point in two-dimensional geometric coordinates'

    def __init__(self, x=0, y=0):
        '''Initialize the position of a new point. The x and y coordinates
        can be specified. If they are not, the point defaults to the origin.'''
        self.move(x, y)

    def move(self, x, y):
        'Move the point to a new location in 2D space.'
        self.x = x
        self.y = y

    def reset(self):
        'Reset the point back to the geometric origin: 0, 0.'
        self.move(0, 0)

    def calculate_distance(self, other_point):
        '''Calculate the distance from this point to a second point passed
        as a parameter.

        This function uses the Pythagorean Theorem to calculate the distance
        between the two points. The distance is returned as a float.'''
        return math.sqrt(
            (self.x - other_point.x) ** 2 +
            (self.y - other_point.y) ** 2
        )

'''
python -i 06\ Explaining\ yourself.py

>>> help(Point)

Help on class Point in module __main__:

class Point(builtins.object)
 |  Represents a point in two-dimensional geometric coordinates
 |
 |  Methods defined here:
 |
 |  __init__(self, x=0, y=0)
 |      Initialize the position of a new point. The x and y coordinates
 |      can be specified. If they are not, the point defaults to the origin.
 |
 |  calculate_distance(self, other_point)
 |      Calculate the distance from this point to a second point passed
 |      as a parameter.
 |
 |      This function uses the Pythagorean Theorem to calculate the distance
 |      between the two points. The distance is returned as a float.
 |
 |  move(self, x, y)
 |      Move the point to a new location in 2D space.
 |
 |  reset(self)
 |      Reset the point back to the geometric origin: 0, 0.
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |
 |  __dict__
 |      dictionary for instance variables (if defined)
 |
 |  __weakref__
 |      list of weak references to the object (if defined)
'''
