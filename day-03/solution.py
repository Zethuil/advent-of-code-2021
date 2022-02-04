from sqlalchemy import false
from sqlalchemy.sql.expression import true


def find_most_frequent_value(input_list, bit_index):
    counter = 0
    for number in input_list:
        counter += 1 if number[bit_index] == "1" else -1

    return "1" if counter >= 0 else "0"


def filter_by_bit(input_list, bit_index, value):
    result_list = []
    for number in input_list:
        if number[bit_index] == value:
            result_list.append(number)

    return result_list


def invert_bits(input_binary):
    output_binary = ""
    output_binary = output_binary.join(
        ["1" if input_binary[i] == "0" else "0" for i in range(len(input_binary))]
    )

    return output_binary


def calculate_advanced_rating(input_list, lower_frequency=False):
    new_list = input_list
    for i in range(len(input_list[0])):
        bit_value = find_most_frequent_value(new_list, i)
        new_list = filter_by_bit(
            new_list, i, invert_bits(bit_value) if lower_frequency else bit_value
        )

        if len(new_list) == 1:
            break

    return new_list[0]


def calculate_oxygen_generator_rating(input_list):

    return calculate_advanced_rating(input_list)


def calculate_co2_scrubber_rating(input_list):

    return calculate_advanced_rating(input_list, lower_frequency=True)


def calculate_life_support_rating(input_list):
    oxygen = calculate_oxygen_generator_rating(input_list)
    scrubber = calculate_co2_scrubber_rating(input_list)

    return int(oxygen, 2) * int(scrubber, 2)


def calculate_gamma_rate(input_list):
    gamma = ""
    for i in range(len(input_list[0])):
        gamma += find_most_frequent_value(input_list, i)

    return gamma


def calculate_epsilon_rate(gamma_rate):

    return invert_bits(gamma_rate)


def calculate_power_consumption(input_list):
    gamma = calculate_gamma_rate(input_list)
    epsilon = calculate_epsilon_rate(gamma)

    return int(gamma, 2) * int(epsilon, 2)


if __name__ == "__main__":
    print("...running")
