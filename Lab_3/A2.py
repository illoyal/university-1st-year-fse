import string

password = input()

allowed = string.ascii_uppercase + string.ascii_lowercase + string.digits + "*,-#"

has_len_err = len(password) != 8
has_upper_err = not any(symbol.isupper() for symbol in password)
has_lower_err = not any(symbol.islower() for symbol in password)
has_digit_err = not any(symbol.isdigit() for symbol in password)
has_spec_err = not any(symbol in "*,-#" for symbol in password)
has_invalid_err = not all(symbol in allowed for symbol in password)

if not (has_len_err or has_upper_err or has_lower_err or has_digit_err or has_spec_err or has_invalid_err):
    print("Надежный пароль")
else:
    if has_len_err:
        print("Длина пароля не равна 8")
    if has_upper_err:
        print("В пароле отсутствуют заглавные буквы")
    if has_lower_err:
        print("В пароле отсутствуют строчные буквы")
    if has_digit_err:
        print("В пароле отсутствуют цифры")
    if has_spec_err:
        print("В пароле отсутствуют специальные символы")
    if has_invalid_err:
        print("В пароле используются непредусмотренные символы")