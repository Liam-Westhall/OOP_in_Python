from two_d_point import TwoDPoint
from typing import Tuple
import math

class Quadrilateral:

    def __init__(self, *floats) -> None:
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])

    @property
    def vertices(self):
        return self.__vertices

    def side_lengths(self) -> Tuple:
        lengths = []
        sides = [self.vertices[i] - self.vertices[(i+1) % len(self.vertices)] for i in range(len(self.vertices))]
        for side in sides:
            lengths.append(math.sqrt(side.x ** 2 + side.y ** 2))
        return tuple(lengths)

    def smallest_x(self) -> float:
        smallest = float("inf")
        for i in self.vertices:
            if i.x < smallest:
                smallest = i.x
        return smallest

    def __eq__(self, other) -> bool:
        return self.side_lengths() == other.side_lengths() and self.smallest_x() == other.smallest_x()

    def __str__(self) -> str:
        return "Quadrilateral: [(%g,%g) (%g, %g) (%g, %g) (%g, %g)]" % (self.vertices[0].x, self.vertices[0].y, self.vertices[1].x, self.vertices[1].y, self.vertices[2].x,self.vertices[2].y, self.vertices[3].x, self.vertices[3].y)
