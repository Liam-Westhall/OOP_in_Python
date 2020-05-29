import unittest
from unittest import TestCase
from square import Square


class TestSquare(TestCase):

    def test_ismemberTrue(self):
        try:
            test_square = Square(1,2,2,2,2,1,1,1)
        except:
            self.fail(test_rectangle, "Wrong")

    def test_is_memberFalse(self):
        try:
            test_rectangle = Square(1,1,1,1,1,1,1,1)
        except:
            self.fail(test_rectangle, "Wrong")

    def test_snap1(self):
        test_square = Square(3.5,1.5,4.5,1.5,4.5,0.5,3.5,0.5)
        result = test_square.snap()
        rightresult = Square(4,2,5,2,5,1, 4 ,1)
        self.assertEqual(result, rightresult, "Error")


    def test_snap2(self):
        test_square = Square(1,2,2,2,2,1,1,1)
        result = test_square.snap()
        rightresult = Square(1,2,2,2,2,1, 1 ,1)
        self.assertEqual(result, rightresult, "Error")

    def test_str(self):
        test_square = Square(1, 2, 2, 2, 2, 1, 1, 1)
        string = str(test_square)
        self.assertEqual("Square: [(1,2) (2, 2) (2, 1) (1, 1)]", string, "Wrong")

    def test_eq(self):
        test_square1 = Square(1, 2, 2, 2, 2, 1, 1, 1)
        test_square2 = Square(1, 2, 2, 2, 2, 1, 1, 1)
        self.assertEqual(test_square2, test_square1, "Wrong")
if __name__ == '__main__':
    unittest.main()
