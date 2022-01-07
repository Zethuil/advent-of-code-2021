# helper function
def convert_to_int_list(str_list):
    return list(map(int, str_list))


# solution to task 1
def count_increases(num_input):
    last_value = None
    counter = 0
    for num in num_input:
        if last_value is not None and num > last_value:
            counter += 1

        last_value = num

    return counter


# solution to task 2
def sliding_window(num_input):
    size = 3
    window_sums = []
    for i in range(len(num_input) - size + 1):
        window_sums.append(sum(num_input[i:i+size]))

    return window_sums


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        test_data = convert_to_int_list(f.readlines())
        sliding_window_list = sliding_window(test_data)

        sliding_window_increases = count_increases(sliding_window_list)

        print(sliding_window_increases)
