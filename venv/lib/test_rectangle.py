import unittest
from unittest import TestCase
from rectangle import Rectangle
from two_d_point import TwoDPoint
class TestRectangle(TestCase):
    def test_is_memberTrue(self):
        try:
            test_rectangle = Rectangle(5,6,7,6,7,1,5,1)
        except:
            self.fail(test_rectangle, "yeet")
    def test_is_memberFalse(self):
        try:
            test_rectangle = Rectangle(1,1,1,1,1,1,1,1)
        except:
            self.fail(test_rectangle, "yes")


    def test_center(self):
        test_rectangle = Rectangle(5,6,7,6,7,1,5,1)
        center = test_rectangle.center()
        point1 = TwoDPoint(6,3.5)
        self.assertEqual(center,point1, "Wrong")


    def test_area(self):
        test_rectangle = Rectangle(5,6,7,6,7,1,5,1)
        area = test_rectangle.area()
        self.assertEquals(10, area, "No")

    def test_str(self):
        test_rectangle = Rectangle(5, 6, 7, 6, 7, 1, 5, 1)
        string = str(test_rectangle)
        self.assertEqual("Rectangle: [(5,6) (7, 6) (7, 1) (5, 1)]", string, "Wrong")
    def test_eq(self):
        test_rectangle1 = Rectangle(5, 6, 7, 6, 7, 1, 5, 1)
        test_rectangle2 = Rectangle(5, 6, 7, 6, 7, 1, 5, 1)
        self.assertEqual(test_rectangle2,test_rectangle1, "Error")
if __name__ == '__main__':
    unittest.main()

