from the_python_code import inc_dec    # The code to test
import unittest   # The test framework

class Test_TestIncrementDecrement(unittest.TestCase):
    def test_increment(self):
        """
        Function should increment the value of x by 1.
        """
        self.assertEqual(inc_dec.increment(3), 4)

    # This test is designed to fail for demonstration purposes.
    def test_decrement(self):
        """
        Function should decrement the value of x by 1.
        """
        self.assertEqual(inc_dec.decrement(3), 4)

if __name__ == '__main__':
    unittest.main()
