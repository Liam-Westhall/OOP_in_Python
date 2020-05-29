import unittest
from unittest import TestCase
from two_d_point import TwoDPoint

class TestTwoDPoint(TestCase):
    def test_from_coordinates(self):
        initial_points = [0,1,2,1,1,1,2,0,]
        points = TwoDPoint.from_coordinates(initial_points)
        rightresultlist = []
        rightresultlist.append(TwoDPoint(0,1))
        rightresultlist.append(TwoDPoint(2,1))
        rightresultlist.append(TwoDPoint(1,1))
        rightresultlist.append(TwoDPoint(2,0))
        self.AssertTrue(points == rightresultlist)

    def test_add(self):
       point1 = TwoDPoint(1,2)
       point2 = TwoDPoint(2,1)
       point3 = TwoDPoint(3,3)
       result = point1 + point2
       self.assertEqual(point3,result,"Wrong")

    def test_sub(self):
        point1 = TwoDPoint(2,2)
        point2 = TwoDPoint(2,0)
        point3 = TwoDPoint(0,2)
        result = point1 - point2
        self.assertEqual(point3,result,"Wrong")

if __name__ == '__main__':
    unittest.main()

