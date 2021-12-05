import unittest

from solution import convert_to_int_list, count_increases, sliding_window


class Day01Test(unittest.TestCase):
    def test_sample_increases(self):
        """
        Test if the sample input yields the right results.
        """
        with open("sample.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())

            # act
            count = count_increases(test_data)

            # assert
            self.assertEqual(count, 7)

    def test_main_increases(self):
        """
        Test if the main input yields the right results.
        """
        with open("input.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())

            # act
            count = count_increases(test_data)

            # assert
            self.assertEqual(count, 1393)

    def test_sliding_window_sample(self):
        with open("sample.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())

            # act
            sliding_window_list = sliding_window(test_data)

            # assert
            self.assertEqual(
                sliding_window_list, [607, 618, 618, 617, 647, 716, 769, 792]
            )

    def test_sliding_window_sample_increases(self):
        with open("sample.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())
            sliding_window_list = sliding_window(test_data)

            # act
            sliding_window_increases = count_increases(sliding_window_list)

            # assert
            self.assertEqual(sliding_window_increases, 5)

    def test_sliding_window_input_increases(self):
        with open("input.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())
            sliding_window_list = sliding_window(test_data)

            # act
            sliding_window_increases = count_increases(sliding_window_list)

            # assert
            self.assertEqual(sliding_window_increases, 1359)


if __name__ == "__main__":
    unittest.main()
