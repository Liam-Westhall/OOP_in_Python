from rectangle import Rectangle
from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint
import math

class Square(Rectangle):
    def __init__(self, *floats) -> None:
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    def __is_member(self) -> bool:
        lengths = []
        sides = [self.vertices[i] - self.vertices[(i+1) % len(self.vertices)] for i in range(len(self.vertices))]
        for side in sides:
            lengths.append(math.sqrt(side.x ** 2 + side.y ** 2))
        for i in range(len(sides)):
            if sides[i].x * sides[(i+1) % len(sides)].x + sides[i].y * sides[(i+1) % len(sides)].y == 0 and all(length == lengths[0] for length in lengths):
                return True
            else:
                return False  # TODO

    def snap(self) -> Quadrilateral:
        snapped_result = []
        for i in self.vertices:
            snapped_result.append(math.floor(i.x + 0.5))
            snapped_result.append(math.floor(i.y + 0.5))
        if all(snaps == snapped_result[0] for snaps in snapped_result):
            return self
        else:
            return Quadrilateral(*snapped_result)  # TODO

    def __eq__(self, other) -> bool:
        return self.side_lengths() == other.side_lengths() and self.smallest_x() == other.smallest_x()

    def __str__(self) -> str:
        return "Square: [(%g,%g) (%g, %g) (%g, %g) (%g, %g)]" % (self.vertices[0].x, self.vertices[0].y, self.vertices[1].x, self.vertices[1].y, self.vertices[2].x, self.vertices[2].y, self.vertices[3].x, self.vertices[3].y)

