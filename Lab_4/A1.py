import random
import time

while True:
    try:
        n = int(input("Введите количество примеров: "))
        if n > 0:
            break
        print("Пожалуйста, введите положительное целое число!")
    except ValueError:
        print("Пожалуйста, введите целое число!")

correct_count = 0
total_start_time = time.time()

for i in range(1, n + 1):
    a = random.randint(2, 9)
    b = random.randint(2, 9)
    correct_ans = a * b

    print(f"\nВопрос {i}/{n}")
    start_time = time.time()

    while True:
        user_input = input(f"{a}*{b}=")
        try:
            answer = int(user_input)
            break
        except ValueError:
            print("Пожалуйста, введите целое число!")

    elapsed_time = time.time() - start_time

    if answer == correct_ans:
        print(f"Верно! (Время: {elapsed_time:.1f} сек)")
        correct_count += 1
    else:
        print(f"Неверно! Правильно: {correct_ans} (Время: {elapsed_time:.1f} сек)")

total_time = time.time() - total_start_time
avg_time = total_time / n
percent = (correct_count / n) * 100

print("\nСТАТИСТИКА:")
print(f"Общее время: {total_time:.1f} секунд")
print(f"Среднее время на вопрос: {avg_time:.1f} сек")
print(f"Правильных ответов: {correct_count}/{n}")
print(f"Процент правильных: {percent:.1f}%")