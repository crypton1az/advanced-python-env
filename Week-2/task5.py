valid_symbols = {'A', 'B', 'C', 'E', 'H', 'K', 'M', 'O', 'P', 'T', 'X', 'Y'}
def check_plate(plate_str):
    if len(plate_str) != 6:
        return False
    if not (plate_str[0] in valid_symbols and plate_str[4] in valid_symbols and plate_str[5] in valid_symbols):
        return False
    if not (plate_str[1].isdigit() and plate_str[2].isdigit() and plate_str[3].isdigit()):
        return False
    return True
plate_count = int(input())
for _ in range(plate_count):
    current_plate = input().strip()
    print("Yes" if check_plate(current_plate) else "No")
