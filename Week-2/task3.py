equation_line = input().strip()
ch1, operator_ch, ch2, _, ch3 = equation_line[0], equation_line[1], equation_line[2], equation_line[3], equation_line[4]
if ch1 == 'x':
    unknown_val = int(ch3) - int(ch2) if operator_ch == '+' else int(ch3) + int(ch2)
elif ch2 == 'x':
    unknown_val = int(ch3) - int(ch1) if operator_ch == '+' else int(ch1) - int(ch3)
else:
    unknown_val = int(ch1) + int(ch2) if operator_ch == '+' else int(ch1) - int(ch2)
print(unknown_val)
