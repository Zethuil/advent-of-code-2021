import unittest

from solution import count_increases


class Day01Test(unittest.TestCase):
    def test_sample_input(self):
        """
        Test if the sample input yields the right results.
        """
        with open("sample.txt", "r") as f:
            # arrange
            test_data = f.readlines()

            # act
            count = count_increases(test_data)

            # assert
            self.assertEqual(count, 7)

    def test_main_input(self):
        """
        Test if the main input yields the right results.
        """
        with open("input.txt", "r") as f:
            # arrange
            test_data = f.readlines()

            # act
            count = count_increases(test_data)

            # assert
            self.assertEqual(count, 1393)


if __name__ == "__main__":
    unittest.main()
