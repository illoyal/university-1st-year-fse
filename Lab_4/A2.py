n = int(input("Введите количество строк прямоугольника (n): "))
m = int(input("Введите количество столбцов прямоугольника (m): "))

print(f"\nПРЯМОУГОЛЬНИК {n}x{m}:")
for i in range(n):
    for j in range(m):
        print("#", end="")
    print()

n_tr = int(input("\nВведите количество строк треугольника (n): "))

print("\nПРАВЫЙ ТРЕУГОЛЬНИК:")
for i in range(1, n_tr + 1):
    for j in range(i):
        print("#", end="")
    print()

n_r = int(input("\nВведите количество строк рамки (n): "))
m_r = int(input("Введите количество столбцов рамки (m): "))

print(f"\nРАМКА {n_r}*{m_r}:")
for i in range(n_r):
    for j in range(m_r):
        if i == 0 or i == n_r - 1 or j == 0 or j == m_r - 1:
            print("#", end="")
        else:
            print(" ", end="")
    print()