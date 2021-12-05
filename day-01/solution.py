def count_increases(text_input):
    last_value = None
    counter = 0
    for num in text_input:
        counter += 0 if last_value is None else (0 if int(num) <= last_value else 1)
        last_value = int(num)

    return counter
