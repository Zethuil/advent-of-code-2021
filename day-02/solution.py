def move_submarine(horizontal_position, depth, direction, aim=None):
    direction_of_movement = direction.split()[0]
    length = int(direction.split()[1])

    if direction_of_movement == "forward":
        horizontal_position += length
        if aim is not None:
            depth += aim * length

    if direction_of_movement == "down":
        if aim is None:
            depth += length  # only needed for part 1
        else:
            aim += length  # only needed for part 2

    if direction_of_movement == "up":
        if aim is None:
            depth -= length  # only needed for part 1
        else:
            aim -= length  # only needed for part 2

    return horizontal_position, depth, aim


if __name__ == "__main__":
    with open("input.txt", "r") as input_file:
        instructions = input_file.readlines()

    horizontal_position, depth, aim = 0, 0, 0
    for instruction in instructions:
        horizontal_position, depth, aim = move_submarine(
            horizontal_position, depth, instruction, aim
        )

    print(horizontal_position, depth, horizontal_position * depth)
