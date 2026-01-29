def all_eq(string_list):
    if not string_list:
        return []
    max_len_val = 0
    for elem in string_list:
        if len(elem) > max_len_val:
            max_len_val = len(elem)
    result_list = []
    for elem in string_list:
        if len(elem) < max_len_val:
            elem = elem + "_" * (max_len_val - len(elem))
        result_list.append(elem)
    return result_list
