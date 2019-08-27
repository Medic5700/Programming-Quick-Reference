# https://docs.python.org/3.5/library/unittest.html#module-unittest
import unittest

class TestA(unittest.TestCase):
    #this class needs to inherit from unittest.TestCase to run the test
    
    def setUp(self):
        #this gets done before every test
        self.array = [i for i in range(0, 10)]
    
    def tearDown(self):
        #this gets done after every test
        del(self.array)
    
    def test1(self):
        """function documentation will be printed in the test results, it helps when figuring out what a failed test does"""
        #this is a test case
        self.assertEqual(self.array, [i for i in range(0, 10)])
    
    def test2(self):
        """test2 discription"""
        #another test case
        self.assertEqual(self.array, [i for i in range(0, 11)]) #this will fail the test
    
    ''' #Short list of asserts
    # https://docs.python.org/3.5/library/unittest.html#classes-and-functions
    assertEqual(a, b)            -> a == b   
    assertNotEqual(a, b)         -> a != b   
    assertTrue(x) bool(x)        -> is True   
    assertFalse(x) bool(x)       -> is False   
    assertIs(a, b)               -> a is b
    assertIsNot(a, b)            -> a is not b
    assertIsNone(x)              -> x is None
    assertIsNotNone(x)           -> x is not None
    assertIn(a, b)               -> a in b
    assertNotIn(a, b)            -> a not in b
    assertIsInstance(a, b)       -> isinstance(a, b)
    assertNotIsInstance(a, b)    -> not isinstance(a, b)
    
    assertAlmostEqual(a, b)      -> round(a-b, 7) == 0   
    assertNotAlmostEqual(a, b)   -> round(a-b, 7) != 0   
    assertGreater(a, b)          -> a > b 
    assertGreaterEqual(a, b)     -> a >= b 
    assertLess(a, b)             -> a < b 
    assertLessEqual(a, b)        -> a <= b 
    assertRegex(s, r)            -> r.search(s) 
    assertNotRegex(s, r)         -> not r.search(s) 
    assertCountEqual(a, b)       -> a and b have the same elements in the same number, regardless of their order
    '''

class TestB(unittest.TestCase):
    #this is another series of tests, you can have as many as you need, as long as they all inherit from 'unittest.TestCase'
    
    def setUp(self):
        #this gets done before every test
        self.array = ['a', 'b', 'c']
    
    def tearDown(self):
        #this gets done after every test
        del(self.array)
        
    def test1(self):
        """test1"""
        #this is a test case
        self.assertEqual(self.array, ['a', 'b', 'c'])    


if __name__ == "__main__":
    unittest.main(verbosity=2, exit=False)
    #by default, unittest.main will exit after completion, it's set here not to exit
    #Set the verbosity to 2, which tells you which test cases are passing/failing more clearly
