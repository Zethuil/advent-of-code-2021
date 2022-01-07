import unittest

from solution import convert_to_int_list, count_increases, sliding_window


class Day01Test(unittest.TestCase):
    def test_sample_increases(self):
        """
        Test that we count the depth increases correctly for the sample data.
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
        Test that we count the depth increases correctly for the sample data.
        """
        with open("input.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())

            # act
            count = count_increases(test_data)

            # assert
            self.assertEqual(count, 1393)

    def test_sliding_window_sample(self):
        """
        Test that we calculate the correct sliding window sum for the sample data.
        """
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
        """
        Test that we calculate the right number of increases for sliding window sums of the sample data.
        """
        with open("sample.txt", "r") as f:
            # arrange
            test_data = convert_to_int_list(f.readlines())
            sliding_window_list = sliding_window(test_data)

            # act
            sliding_window_increases = count_increases(sliding_window_list)

            # assert
            self.assertEqual(sliding_window_increases, 5)

    def test_sliding_window_input_increases(self):
        """
        Test that we calculate the right number of increases for sliding window sums of the main data.
        """
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
