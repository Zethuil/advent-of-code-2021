import unittest

from solution import move_submarine


class Day02Test(unittest.TestCase):
    def test_single_move_forward(self):
        # arrange
        horizontal_position, depth = 0, 0

        # act
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, "forward 5"
        )

        # assert
        self.assertEqual(horizontal_position, 5)

    def test_single_move_down(self):
        # arrange
        horizontal_position, depth = 0, 0

        # act
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, "down 5"
        )

        # assert
        self.assertEqual(depth, 5)

    def test_single_move_up(self):
        # arrange
        horizontal_position, depth = 0, 5

        # act
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, "up 5"
        )

        # assert
        self.assertEqual(depth, 0)

    def test_sample_input(self):
        # arrange
        horizontal_position, depth = 0, 0
        with open("sample.txt", "r") as input_file:
            instructions = input_file.readlines()

        # act
        for instruction in instructions:
            horizontal_position, depth, aim = move_submarine(
                horizontal_position, depth, instruction
            )

        # assert
        self.assertEqual(horizontal_position, 15)
        self.assertEqual(depth, 10)

    def test_main_input(self):
        # arrange
        horizontal_position, depth = 0, 0
        with open("input.txt", "r") as input_file:
            instructions = input_file.readlines()

        # act
        for instruction in instructions:
            horizontal_position, depth, aim = move_submarine(
                horizontal_position, depth, instruction
            )

        # assert
        self.assertEqual(horizontal_position, 1845)
        self.assertEqual(depth, 916)

    def test_aim_down(self):
        # arrange
        horizontal_position, depth, aim = 0, 0, 0

        # act
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, "down 5", aim
        )

        # assert
        self.assertEqual(aim, 5)

    def test_aim_up(self):
        # arrange
        horizontal_position, depth, aim = 0, 0, 5

        # act
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, "up 5", aim
        )

        # assert
        self.assertEqual(aim, 0)

    def test_aim_forward(self):
        # arrange
        horizontal_position, depth, aim = 5, 5, 5

        # act
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, "forward 8", aim
        )

        # assert
        self.assertEqual(horizontal_position, 13)
        self.assertEqual(depth, 45)
        self.assertEqual(aim, 5)

    def test_sample_input_with_aim(self):
        # arrange
        horizontal_position, depth, aim = 0, 0, 0
        with open("sample.txt", "r") as input_file:
            instructions = input_file.readlines()

        # act
        for instruction in instructions:
            horizontal_position, depth, aim = move_submarine(
                horizontal_position, depth, instruction, aim
            )

        # assert
        self.assertEqual(horizontal_position, 15)
        self.assertEqual(depth, 60)

    def test_main_input_with_aim(self):
        # arrange
        horizontal_position, depth, aim = 0, 0, 0
        with open("input.txt", "r") as input_file:
            instructions = input_file.readlines()

        # act
        for instruction in instructions:
            horizontal_position, depth, aim = move_submarine(
                horizontal_position, depth, instruction, aim
            )

        # assert
        self.assertEqual(horizontal_position, 1845)
        self.assertEqual(depth, 763408)


if __name__ == "__main__":
    unittest.main()
