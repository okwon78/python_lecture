import unittest
from UnitTest import calc


# plz, refer to following document
# https://docs.python.org/3/library/unittest.html#unittest.TestCase.debug

class TestCalc(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setupClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    # pre condition
    def setUp(self):
        print('setUp')

    # post condition
    def tearDown(self):
        print('TearDown')

    # the name of method should start with 'test_'. if not, unit test wouldn't work
    def test_add(self):
        print('add')
        self.assertEqual(calc.add(10, 5), 15)
        self.assertEqual(calc.add(0, 5), 5)
        self.assertEqual(calc.add(-1, -1), -2)

    def test_sub(self):
        print('sub')
        self.assertEqual(calc.sub(10, 5), 5)
        self.assertEqual(calc.sub(-1, -1), 0)


if __name__ == '__main__':
    unittest.main()