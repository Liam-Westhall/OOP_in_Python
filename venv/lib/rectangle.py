from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint


class Rectangle(Quadrilateral):

    def __init__(self, *floats) -> None:
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

    def __is_member(self) -> bool:
        sides = [self.vertices[i] - self.vertices[(i+1) % len(self.vertices)] for i in range(len(self.vertices))]
        for i in range(len(sides)):
            if sides[i].x * sides[(i+1) % len(sides)].x + sides[i].y * sides[(i+1) % len(sides)].y == 0:
                return True
            else:
                return False  # TODO

    def center(self) -> TwoDPoint:
        centerx = (self.vertices[0].x + self.vertices[2].x)/2
        centery = (self.vertices[0].y + self.vertices[2].y)/2
        centerpoint = TwoDPoint(centerx, centery)
        return centerpoint

    def area(self) -> int:
        side_lengths = self.side_lengths()
        return side_lengths[0] * side_lengths[1]

    def __eq__(self, other) -> bool:
        return self.area() == other.area() and self.center() == other.center()

    def __str__(self) -> str:
        return "Rectangle: [(%g,%g) (%g, %g) (%g, %g) (%g, %g)]" % ( self.vertices[0].x, self.vertices[0].y, self.vertices[1].x, self.vertices[1].y, self.vertices[2].x,self.vertices[2].y, self.vertices[3].x, self.vertices[3].y)
