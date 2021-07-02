import unittest
from duplicate_zeros import Solution


class DuplicateZerosTest(unittest.TestCase):

   def setUp(self):
       self.obj = Solution()

   def test_duplicate_zeros1(self):
       arr = [1,2,3]
       self.obj.duplicateZeros(arr)

       self.assertEqual([1,2,3], self.obj.arr)



   def test_duplicate_zeros2(self):
       arr = [1,0,2,3,0,4,5,0]
       self.obj.duplicateZeros(arr)

       self.assertEqual([1,0,0,2,3,0,0,4], self.obj.arr)


   def test_duplicate_zeros3(self):
       arr = [1,0,5,7,8,0]
       self.obj.duplicateZeros(arr)

       self.assertEqual([1,0,0,5,7,8], self.obj.arr)


   def test_duplicate_zeros4(self):
       arr = [0,4,1,0,0,8,0,0,3]
       self.obj.duplicateZeros(arr)

       self.assertEqual([0,0,4,1,0,0,0,0,8], self.obj.arr)


