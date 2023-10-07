# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# Press the green button in the gutter to run the script.
import unittest
from Core import *


class TrialOfTheGods(unittest.TestCase):

    # Define your test methods as functions starting with "test_"

    # Test HelloGods function
    def test_HelloGods(self):
        result = HelloGods()
        expected = "Hello Gods !"
        self.assertEqual(result, expected)
        print("HelloGods-test1: Ok" if result == expected else "HelloGods-test1: Fail")

    # Test MyGodAge function
    def test_MyGodAge(self):
        result1 = MyGodAge(25, "Zeus")
        expected1 = 4 * 42 + 25
        self.assertEqual(result1, expected1)
        print("MyGodAge-test1: Ok" if result1 == expected1 else "MyGodAge-test1: Fail")

        result2 = MyGodAge(18, "Athena")
        expected2 = 6 * 42 + 18
        self.assertEqual(result2, expected2)
        print("MyGodAge-test2: Ok" if result2 == expected2 else "MyGodAge-test2: Fail")

        result3 = MyGodAge(30, "")
        expected3 = -1
        self.assertEqual(result3, expected3)
        print("MyGodAge-test3: Ok" if result3 == expected3 else "MyGodAge-test3: Fail")

        result4 = MyGodAge(-10, "Hades")
        expected4 = -1
        self.assertEqual(result4, expected4)
        print("MyGodAge-test4: Ok" if result4 == expected4 else "MyGodAge-test4: Fail")

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
    # Create a test suite
    suite = unittest.TestLoader().loadTestsFromTestCase(TrialOfTheGods)

    # Run the tests and print the results
    result = unittest.TextTestRunner(verbosity=2).run(suite)

    # Check if all tests passed
    if result.wasSuccessful():
        print("All tests passed!")
    else:
        print("Some tests failed.")
