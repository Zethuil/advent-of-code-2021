import unittest

from solution import (
    calculate_gamma_rate,
    calculate_epsilon_rate,
    calculate_life_support_rating,
    calculate_power_consumption,
    filter_by_bit,
    calculate_oxygen_generator_rating,
    calculate_co2_scrubber_rating,
)


class Day03Test(unittest.TestCase):
    def test_simple_input_gamma_rate(self):
        # arrange
        input_list = ["00100", "11110", "10110"]

        # act
        gamma_rate = calculate_gamma_rate(input_list)

        # assert
        self.assertEqual(gamma_rate, "10110")

    def test_simple_epsilon_rate(self):
        # arrange
        input_list = ["00100", "11110", "10110"]
        gamma_rate = calculate_gamma_rate(input_list)

        # act
        epsilon_rate = calculate_epsilon_rate(gamma_rate)

        # assert
        self.assertEqual(epsilon_rate, "01001")

    def test_sample_input_gamma_rate(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        gamma_rate = calculate_gamma_rate(input_list)

        # assert
        self.assertEqual(gamma_rate, "10110")

    def test_sample_input_epsilon_rate(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()
            gamma_rate = calculate_gamma_rate(input_list)

        # act
        epsilon_rate = calculate_epsilon_rate(gamma_rate)

        # assert
        self.assertEqual(epsilon_rate, "01001")

    def test_sample_input_power_consumption(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        power_consumption = calculate_power_consumption(input_list)

        # assert
        self.assertEqual(power_consumption, 198)

    def test_main_input_power_consumption(self):
        # arrange
        with open("input.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        power_consumption = calculate_power_consumption(input_list)

        # assert
        self.assertEqual(power_consumption, 693486)

    def test_sample_input_filter_by_bit(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        actual_list = filter_by_bit(input_list, 0, "1")

        # assert
        self.assertEqual(
            actual_list, ["11110", "10110", "10111", "10101", "11100", "10000", "11001"]
        )

    def test_sample_input_oxygen_rating(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        actual = calculate_oxygen_generator_rating(input_list)

        # assert
        self.assertEqual(actual, "10111")

    def test_sample_input_scrubber_rating(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        actual = calculate_co2_scrubber_rating(input_list)

        # assert
        self.assertEqual(actual, "01010")

    def test_sample_input_life_support_rating(self):
        # arrange
        with open("sample.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        actual = calculate_life_support_rating(input_list)

        # assert
        self.assertEqual(actual, 230)

    def test_main_input_life_support_rating(self):
        # arrange
        with open("input.txt", "r") as input_file:
            input_list = input_file.read().splitlines()

        # act
        actual = calculate_life_support_rating(input_list)

        # assert
        self.assertEqual(actual, 3379326)


if __name__ == "__main__":
    unittest.main()