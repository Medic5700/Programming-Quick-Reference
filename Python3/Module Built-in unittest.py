"""
References:
    https://docs.python.org/3/library/unittest.html
    https://www.youtube.com/watch?v=6tNS--WetLI (Python Tutorial: Unit Testing Your Code with the unittest Module)[Corey Schafer]
"""
"""
Available asserts
note: all asserts take an additional extra message argument
#Common asserts
    assertEqual(a, b)                               a == b
    assertNotEqual(a, b)                            a != b
    assertTrue(x)                                   bool(x) is True
    assertFalse(x)                                  bool(x) is False
    assertIs(a, b)                                  a is b
    assertIsNot(a, b)                               a is not b
    assertIsNone(x)                                 x is None
    assertIsNotNone(x)                              x is not None
    assertIn(a, b)                                  a in b
    assertNotIn(a, b)                               a not in b
    assertIsInstance(a, b)                          isinstance(a, b)
    assertNotIsInstance(a, b)                       not isinstance(a, b)
#exception asserts
    assertRaises(exc, fun, *args, **kwds)           fun(*args, **kwds) raises exc
    assertRaisesRegex(exc, r, fun, *args, **kwds)   fun(*args, **kwds) raises exc and the message matches regex r
    assertWarns(warn, fun, *args, **kwds)           fun(*args, **kwds) raises warn
    assertWarnsRegex(warn, r, fun, *args, **kwds)   fun(*args, **kwds) raises warn and the message matches regex r
    assertLogs(logger, level)                       The with block logs on logger with minimum level
#less common asserts
    assertAlmostEqual(a, b)                         round(a-b, 7) == 0
    assertNotAlmostEqual(a, b)                      round(a-b, 7) != 0
    assertGreater(a, b)                             a > b
    assertGreaterEqual(a, b)                        a >= b
    assertLess(a, b)                                a < b
    assertLessEqual(a, b)                           a <= b
    assertRegex(s, r)                               r.search(s)
    assertNotRegex(s, r)                            not r.search(s)
    assertCountEqual(a, b)                          a and b have the same elements in the same number, regardless of their order.
#type specific asserts, automatically invoked by assertEqual(), but included here for completion
    assertMultiLineEqual(a, b)                      strings
    assertSequenceEqual(a, b)                       sequences
    assertListEqual(a, b)                           lists
    assertTupleEqual(a, b)                          tuples
    assertSetEqual(a, b)                            sets or frozensets
    assertDictEqual(a, b)                           dicts
"""

from time import sleep
from typing import List
import unittest

# Note: the class name for testing doesn't need to start with 'Test', I'm just using 'TestA' for no particular reason
class TestA(unittest.TestCase): # You need to create a class and inherit from 'unittest.TestCase' for the tests to be 'discovered' by the unittest module
    """The Basics"""
    def testA1(self): # test functions NEED to start with 'test' for the unittest module to 'discover' the tests to run
        """Note: function docstrings will be shown if verbose=2"""
        self.assertEqual(True, True) # a success
    def testA2(self):
        self.assertEqual(True, False) # a fail
    def testA3(self): # Note: test functions are not run in any particular order
        print("testA3 output, since this test succedes, this will be printed iff 'buffer' was not set when calling unittest.main()") 
        # output to stdout will NOT be discarded, and will print to the terminal unless unittest.main(buffer=True)
        self.assertEqual(True, True)
    def testA4(self):
        print("testA4 output, this will print regardless of buffer level because this test fails")
        # when unittest.main(buffer=True), output will be echoed in the error message IF the test fails
        self.assertEqual(True, False) # a fail
    def notATest(self): # this function will not run as the function name does not start with 'test'
        self.assertEqual(True, False)

class TestB(unittest.TestCase):
    """Multiple Tests per test function"""
    def testB1(self):
        sleep(1)
        self.assertEqual(True, True, "testB1-1") # a message string
        self.assertEqual(True, True, "testB1-2") # multiple asserts in one fucntion. Note: only one indicator is used for each function. IE: you'll see one success per function, not one success per assert
    def testB2(self):
        sleep(1)
        self.assertEqual(True, True, "testB2-1")
        self.assertEqual(True, False, "testB2-2") # a fail, one fail will stop the function execution and report a fail for that function
        self.assertEqual(True, True, "testB2-3")
    def testB3(self):
        # https://docs.python.org/3/library/unittest.html#distinguishing-test-iterations-using-subtests
        for i in range(8):
            with self.subTest(i = i):
                '''
                this allows running multiple tests and NOT stopping the testing with one failure. 
                Mainly used to tests that have litte variation, like testing a function with slightly different peramiters
                The failure shown will show the itteration numer as well
                Note: (i = i) can be anything, such as (j = j) or (i=i, j=j, ...) or etc. will show up as "FAIL: testB3 (__main__.TestB) (i=6)"
                '''
                self.assertEqual(True, i not in [5, 6], "testB3") # will fail on i == 5, i == 6
    def testB4(self):
        """Nested subTest"""
        for i in range(8):
            with self.subTest(i=i):
                for j in range(8):
                    with self.subTest(j=j):
                        self.assertEqual(True, i != 5 or j != 5, "testB4") # This will fail when i==5 and j==6

class TestC(unittest.TestCase):
    """Exception handling"""
    def foo(self, _):
        """A function that raises an Exception"""
        raise Exception()

    def testC1(self):
        raise Exception() # unhandled Exceptions are caught by the module and will show up in the test report as an error
        self.assertEqual(True, True)
    def testC2(self):
        self.assertEqual(5, self.foo(5)) # unhandled Exceptions are caught by the module and will show up in the test report as an error
    def testC3(self):
        self.assertRaises(Exception, self.foo, 5) # This checks that an Exception is raised, and will show up as a test success
        # Note that you also have to pass in the function arguments as additional arguments to self.asserRaises

class TestD(unittest.TestCase):
    """Demonstrate setUp() and tearDown()
    
    https://docs.python.org/3/library/unittest.html#organizing-test-code
    """
    def setUp(self):
        """setUp() runs before/at the beginning of each test function to set stuff up individually for each test functions"""
        self.array : List[int] = [1, 2, 3]
    def tearDown(self):
        """tearDown runs after each test function"""
        # useful for stuff like closing a file
        pass # 'self.array' does not need to be torn down, as each test function gets it to be reinitialized as though it's a new class instance. Figured it would be a bad example.

    def testD1(self):
        self.array.append(4)
        self.assertEqual(self.array, [1, 2, 3, 4])
    def testD2(self):
        self.array.append(5)
        self.assertEqual(self.array, [1, 2, 3, 5])
    
if __name__ == "__main__":
    
    # unittest.main() #This will run the test cases. Note: will exit python upon completion

    # Some options
    unittest.main(verbosity=2) # setting verbosity to 2 will show additional information, 0 will only show failed tests. (default is 2)
    unittest.main(exit=False) # This will prevent calling of sys.exit() upon completion
    unittest.main(buffer=True) # Will caputure STDOUT output and only echo it when a test fails
