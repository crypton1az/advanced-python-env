1)
shape = input("Enter shape (circle/rectangle/triangle): ")

if shape == "circle":
    r = float(input("Radius: "))
    area = 3.14 * r * r
    print(area)

elif shape == "rectangle":
    a = float(input("Side A: "))
    b = float(input("Side B: "))
    print(a * b)

elif shape == "triangle":
    h = float(input("Height: "))
    b = float(input("Base: "))
    print(0.5 * h * b)

2)
for arr_num in range(3):
    data = input().split()
    total = 0

    for x in data:
        total += int(x)

    avg = total / len(data)
    print("Sum:", total)
    print("Average:", avg)
