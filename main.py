import unittest
from Core import *


class PythonTrial(unittest.TestCase):

    # Define your test methods as functions starting with "test_"

    # Test Hello function
    def test_Hello(self):
        result = Hello()
        expected = "Hello sir !"
        self.assertEqual(result, expected)
        print("Hello-test1: Ok" if result == expected else "Hello-test1: Fail")

    # Test MyAge function
    def test_MyAge(self):
        result1 = MyAge(25, "Zeus")
        expected1 = 4 * 42 + 25
        self.assertEqual(result1, expected1)
        print("MyAge-test1: Ok" if result1 == expected1 else "MyAge-test1: Fail")

        result2 = MyAge(18, "Athena")
        expected2 = 6 * 42 + 18
        self.assertEqual(result2, expected2)
        print("MyAge-test2: Ok" if result2 == expected2 else "MyAge-test2: Fail")

        result3 = MyAge(30, "")
        expected3 = -1
        self.assertEqual(result3, expected3)
        print("MyAge-test3: Ok" if result3 == expected3 else "MyAge-test3: Fail")

        result4 = MyAge(-10, "Hades")
        expected4 = -1
        self.assertEqual(result4, expected4)
        print("MyAge-test4: Ok" if result4 == expected4 else "MyAge-test4: Fail")

    # Test MyPow function
    def test_MyPow(self):
        result1 = MyPow(2, 3)
        expected1 = 8.0
        self.assertAlmostEqual(result1, expected1)
        print("MyPow-test1: Ok" if result1 == expected1 else "MyPow-test1: Fail")

        result2 = MyPow(5, -2)
        expected2 = 0.04
        self.assertAlmostEqual(result2, expected2)
        print("MyPow-test2: Ok" if result2 == expected2 else "MyPow-test2: Fail")

    # Test Facto function
    def test_Facto(self):
        result1 = Facto(5)
        expected1 = 120
        self.assertEqual(result1, expected1)
        print("Facto-test1: Ok" if result1 == expected1 else "Facto-test1: Fail")

        result2 = Facto(0)
        expected2 = 1
        self.assertEqual(result2, expected2)
        print("Facto-test2: Ok" if result2 == expected2 else "Facto-test2: Fail")

        result3 = Facto(-2)
        expected3 = -1
        self.assertEqual(result3, expected3)
        print("Facto-test3: Ok" if result3 == expected3 else "Facto-test3: Fail")

    # Add more test methods as needed


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(PythonTrial)

    result = unittest.TextTestRunner(verbosity=0).run(suite)

    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")
