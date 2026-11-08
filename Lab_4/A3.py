while True:
    packets = input("Введите последовательность (только 0 и 1, длина >= 5): ").strip()
    if len(packets) >= 5 and all(char in '01' for char in packets):
        break
    print("Ошибка! Длина должна быть не менее 5 символов и содержать только 0 и 1.")

total_packets = len(packets)
lost_packets = packets.count('0')

max_zero_sequence = 0
current_zero_sequence = 0

for packet in packets:
    if packet == '0':
        current_zero_sequence += 1
        if current_zero_sequence > max_zero_sequence:
            max_zero_sequence = current_zero_sequence
    else:
        current_zero_sequence = 0

loss_percentage = (lost_packets / total_packets) * 100

if loss_percentage <= 1:
    quality = "отличное качество"
elif loss_percentage <= 5:
    quality = "хорошее качество"
elif loss_percentage <= 10:
    quality = "удовлетворительное качество"
elif loss_percentage <= 20:
    quality = "плохое качество"
else:
    quality = "критическое состояние сети"

print(f"\nОбщее количество пакетов: {total_packets}")
print(f"Количество потерянных пакетов: {lost_packets}")
print(f"Длина самой длинной последовательности потерянных пакетов: {max_zero_sequence}")
print(f"Процент потерь: {loss_percentage:.1f}%")
print(f"Качество связи: {quality}")