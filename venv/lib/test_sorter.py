import unittest
from unittest import TestCase
from sorter import Sorter
from quadrilateral import Quadrilateral
from rectangle import Rectangle
class TestShapeSorter(TestCase):
        def test_sort1(self):
            shape1 = Quadrilateral(-1,1,1,1,2,3,4,5,3,2)
            shape2 = Quadrilateral(0,1,2,3,1,2,3,2,1,5)
            shape3 = Quadrilateral(1,1,2,3,4,5,6,7,8,9)
            shape4 = Quadrilateral(2,1,2,3,4,5,6,7,8,9)
            result = Sorter.sort(shape1,shape2,shape3,shape4)
            rightlist = [shape1,shape2,shape3,shape4]
            self.assertEqual(result, rightlist, "Wrong")
        def test_sort2(self):
            shape1 = Quadrilateral(5,4,3,2,1,4,5,6)
            shapelist = [shape1]
            result = Sorter.sort(shape1)
            self.assertEqual(result, shapelist, "Wrong")

        def test_sort3(self):
            shape1 = Quadrilateral(10,3,2,6,7,8,-5,4)
            shape2 = Rectangle(5,6,7,6,7,1,5,1)
            shape3 = Quadrilateral(5,3,2,6,-4,3,-4,8)
            shape4 = Quadrilateral(4,3,5,1,2,3,2,1)
            result = Sorter.sort(shape1,shape2,shape3,shape4)
            rightlist = [shape1,shape3, shape4, shape2]
            self.assertEqual(result, rightlist, "Wrong")

        def test_sort4(self):
            shape1 = Quadrilateral(1,2,2,2,1,2,1,1)
            shape2 = Quadrilateral(5,6,8,6,7,3,4,5)
            shape3 = Quadrilateral(1,10,5,10,5,5,1,5)
            shape4 = Quadrilateral(2,3,5,3,5,1,2,1)
            result = Sorter.sort(shape1, shape2, shape3, shape4)
            rightlist = [shape1,shape3, shape4, shape2]
            self.assertEqual(result, rightlist, "Wrong")

if __name__ == '__main__':
    unittest.main()
