def is_anagram(str1, str2):
    if len(str1) != len(str2):
        return "NO"
    count_dict = {}
    for ch in str1:
        count_dict[ch] = count_dict.get(ch, 0) + 1
    for ch in str2:
        if ch not in count_dict:
            return "NO"
        count_dict[ch] -= 1
        if count_dict[ch] < 0:
            return "NO"
    for count_val in count_dict.values():
        if count_val != 0:
            return "NO"
    return "YES"
first_string = input().strip()
second_string = input().strip()
print(is_anagram(first_string, second_string))
