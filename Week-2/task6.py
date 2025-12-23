def make_equal_length(string_list):
    max_length_val = max(len(elem) for elem in string_list) if string_list else 0
    return [elem + "_" * (max_length_val - len(elem)) for elem in string_list]
