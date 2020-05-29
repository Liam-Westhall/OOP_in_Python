import unittest
from unittest import TestCase
from quadrilateral import Quadrilateral

class TestQuadrilateral(TestCase):

    def test_side_lengths(self):
        test_quadrilateral = Quadrilateral(0,1,1,1,1,0,0,0)
        side_lengths = test_quadrilateral.side_lengths()
        rightside_lengths = (1,1,1,1)
        self.assertEqual(rightside_lengths, side_lengths, "Wrong")

    def test_smallest_x(self):
        test_quadrilateral = Quadrilateral(0,1,1,1,1,0,0,0)
        smallest_x = test_quadrilateral.smallest_x()
        self.assertEqual(smallest_x, 0, "Wrong")


    def test_eq(self):
        test_quadrilateral1 = Quadrilateral(0, 1, 1, 1, 1, 0, 0, 0)
        test_quadrilateral2 = Quadrilateral(0, 1, 1, 1, 1, 0, 0, 0)
        self.assertEqual(test_quadrilateral1, test_quadrilateral2, "Wrong")

    def test_str(self):
        test_quadrilateral1 = Quadrilateral(0, 1, 1, 1, 1, 0, 0, 0)
        string = str(test_quadrilateral1)
        self.assertEqual("Quadrilateral: [(0,1) (1, 1) (1, 0) (0, 0)]", string)
if __name__ == '__main__':
    unittest.main()
