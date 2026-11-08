def check_luhn(card_number):
    total_sum = 0
    reversed_digits = card_number[::-1]

    for i in range(len(reversed_digits)):
        digit = int(reversed_digits[i])
        if i % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total_sum += digit

    return total_sum % 10 == 0


card_number = input("Введите номер банковской карты: ").strip()

if not card_number.isdigit():
    print("Ошибка: Номер карты должен содержать только цифры!")
else:
    length = len(card_number)
    card_type = "Неизвестный тип"
    is_valid_type_and_len = False

    if (card_number.startswith("34") or card_number.startswith("37")) and length == 15:
        card_type = "American Express"
        is_valid_type_and_len = True
    elif any(card_number.startswith(pref) for pref in ["51", "52", "53", "54", "55"]) and length == 16:
        card_type = "MasterCard"
        is_valid_type_and_len = True
    elif card_number.startswith("4") and (length == 13 or length == 16):
        card_type = "Visa"
        is_valid_type_and_len = True

    if is_valid_type_and_len and check_luhn(card_number):
        print(f"Карта действительна! Тип карты: {card_type}")
    else:
        print("Карта недействительна!")