sequence_input = input().strip()
arrow_counter = 0
for idx in range(len(sequence_input) - 4):
    substring_5 = sequence_input[idx:idx+5]
    if substring_5 == '>>-->' or substring_5 == '<--<<':
        arrow_counter += 1
print(arrow_counter)
