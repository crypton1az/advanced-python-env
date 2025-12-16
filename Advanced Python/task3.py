A = input()

integer_part, fractional_part = A.split('.')
new_number = fractional_part + "." + integer_part
print(new_number)
