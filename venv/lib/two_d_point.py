from typing import List


class TwoDPoint:

    def __init__(self, x, y) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float :
        return self.__y

    def __eq__(self, other: object) -> bool:
        return (self.x == other.x and self.y == other.y)  # TODO

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __str__(self) -> str:
        return '(%g, %g)' % (self.__x, self.__y)

    def __add__(self, other) -> 'TwoDPoint':
        return TwoDPoint(self.x + other.x, self.y + other.y)

    def __sub__(self, other) -> 'TwoDPoint':
        return TwoDPoint(self.x - other.x, self.y - other.y)


    @staticmethod
    def from_coordinates(coordinates: List[float]) -> List['TwoDPoint']:
        if len(coordinates) % 2 != 0:
            raise Exception("Odd number of floats given to build a list of 2-d points")
        points = []
        it = iter(coordinates)
        for x in it:
            points.append(TwoDPoint(x, next(it)))
        return points
