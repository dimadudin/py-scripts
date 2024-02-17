def get_num_guesses(length):
    if length == 1:
        return 26
    return 26 * (get_num_guesses(length - 1) + 1)
