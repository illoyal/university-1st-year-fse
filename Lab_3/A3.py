prev = int(input())
curr = int(input())

if curr >= prev:
    used = curr - prev
else:
    used = (10000 - prev) + curr

if used <= 300:
    cost = 21.0
elif used <= 600:
    cost = 21.0 + (used - 300) * 0.06
elif used <= 800:
    cost = 21.0 + 300 * 0.06 + (used - 600) * 0.04
else:
    cost = 21.0 + 300 * 0.06 + 200 * 0.04 + (used - 800) * 0.025

avg_price = cost / used if used > 0 else 0.0

print(f"Предыдущее\n{prev}")
print(f"Текущее\n{curr}")
print(f"Использовано\n{used}")
print(f"К оплате\n{cost:.2f}")
print(f"Ср. цена m^3\n{avg_price:.2f}")