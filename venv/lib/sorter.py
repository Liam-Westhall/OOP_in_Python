from quadrilateral import Quadrilateral
from two_d_point import TwoDPoint
from typing import List

class Sorter:
    @staticmethod
    def sort(*args) -> List[TwoDPoint]:
        result = list(args)
        def getsmallestx(x):
            return x.smallest_x()
        result.sort(key = getsmallestx)
        return result
