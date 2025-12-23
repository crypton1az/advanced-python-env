string_a = input().strip()
string_b = input().strip()
len_a, len_b = len(string_a), len(string_b)
shifted_set = set()
for start_idx in range(len_b):
    shifted_set.add(string_b[start_idx:] + string_b[:start_idx])
match_count = 0
for pos in range(len_a - len_b + 1):
    if string_a[pos:pos+len_b] in shifted_set:
        match_count += 1
print(match_count)
