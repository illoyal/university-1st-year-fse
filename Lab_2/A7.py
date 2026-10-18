x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

# Находим остаток (0 — четная сумма/белая, 1 — нечетная сумма/черная)
color1 = (x1 + y1) % 2
color2 = (x2 + y2) % 2

# Проверяем, совпадает ли цвет клеток
same_color = (color1 == color2)

# Выводим YES или NO
print(["NO", "YES"][same_color])

# Если цвета совпадают (same_color == True/1), выводим название цвета.
# Если не совпадают (same_color == False/0), этот принт ничего не выведет.
print(["", ["White", "Black"][color1]][same_color])
